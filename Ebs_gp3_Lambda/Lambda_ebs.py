import json
import boto3

def arn_separation(volume_arn): #function used seperate volume arn from cloud watch events 

    arn_parts = volume_arn.split(':')

    volume_id = arn_parts[-1].split('/')[-1]

    return volume_id


def lambda_handler(event, context):
    
    volume_arn = event['resources'][0]

    volume_id = arn_separation(volume_arn)

    ec2_client = boto3.client('ec2')

    response = ec2_client.modify_volume(        #convert the gp2 volume to gp3 volume
        VolumeId=volume_id,
        VolumeType='gp3',
    )
