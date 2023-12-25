#!/bin/bash

#killing the old mongod process
echo " killing old pids"
mongod_pids=$(pgrep mongod)
if [ -n "$mongod_pids" ]; then
  echo "Killing MongoDB processes with PIDs: $mongod_pids"
  kill -15 $mongod_pids
else
  echo "No MongoDB processes found."
fi

sleep 10

DATA_DIR="/var/lib/mongodb"
MEM="1"

#creating members
echo "creating 3 replica members"
MEMBER1="27017"
MEMBER2="27018"
MEMBER3="27019"

#setting replica set name in mongod.conf
echo "setting replica set name in mongod.conf"
file="/etc/mongod.conf"
if ! grep -q "replSetName:" "$file"; then

    echo "replication:
   replSetName: \"rs0\" " >> /etc/mongod.conf
fi

#disabling javascript
echo "disabling java script"
if ! grep -q "javascriptEnabled" "$file"; then

    echo "security:
   javascriptEnabled: false " >> /etc/mongod.conf
fi

#configuring wiredTigerCacheSize as 1GB
conf="--replSet rs0 --wiredTigerCacheSizeGB=$MEM --fork"

#creating new directories
echo "creating new directories for replicas"
mkdir -p $DATA_DIR/{$MEMBER1,$MEMBER2,$MEMBER3}

#initializing the replica

echo " creating the first replica"
mongod --port $MEMBER1 --dbpath $DATA_DIR/$MEMBER1 --logpath $DATA_DIR/$MEMBER1/mongod1.log $conf
sleep 5

echo " creating the second replica"
mongod --port $MEMBER2 --dbpath $DATA_DIR/$MEMBER2 --logpath $DATA_DIR/$MEMBER2/mongod2.log $conf
sleep 5

echo " creating the third replica"
mongod --port $MEMBER3 --dbpath $DATA_DIR/$MEMBER3 --logpath $DATA_DIR/$MEMBER3/mongod3.log $conf
sleep 5

# Initialize replica set marking the 3 replica as arbiter
echo "iniInitialize replica set marking the 3 replica as arbiter"
mongo --port 27017 --eval 'rs.initiate({"_id":"rs0", "members":[{"_id":0,"host":"localhost:27017"}, {"_id":1,"host":"localhost:27018"}, {"_id":2,"host":"localhost:27019", "arbiterOnly": true}] })'
