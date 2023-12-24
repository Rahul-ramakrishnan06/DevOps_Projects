from flask import Flask,request, jsonify
import requests
from requests.auth import HTTPBasicAuth
import json
from github import Github

app = Flask(__name__)  # creating flask application instance

@app.route("/createjira", methods=['POST'])
def github_webhook():
    data = request.get_json()
    comment_body = data['comment']['body']
    
    if '/jira' in comment_body:
    
        createjiraticket(comment_body)
        
    return jsonify({'message': 'Webhook received successfully'})

def createjiraticket(comment_body):

    url = "https://rahulkarthi0602.atlassian.net/rest/api/3/issue"

    API_TOKEN = "ATATT3xFfGF0QcQkZHKUb4TehjNCFoPW7X7pdRmWXUM8qqetcFLj_xG-dvlzQ7yT3zGB_c9HZmNt7xaUFJ6Ght7rZZuBovMZtm2VcEgUaop6rr8ofAKd5ezVpvsqZQUqtP9yQC12SOzX7xmTZVTtw8F_EE2jY_PaB3qlsdQcvzy_fOE3YPVNk0c=FD9A071E"
    auth = HTTPBasicAuth("rahulkarthi06.02@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
    "description": {
        "content": [
            {
            "content": [
                {
                "text": "First issue in jira automation project",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },

 
        "issuetype": {
        "id": "10007"
        },

        "project": {
        "id": "10001"
        },
        "summary": "First issue in jira",
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    
    return json.dumps (json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)
