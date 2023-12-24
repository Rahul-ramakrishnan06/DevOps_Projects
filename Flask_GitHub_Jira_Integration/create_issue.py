from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)  # creating flask application instance

@app.route("/createjira", methods=['POST'])

def createjiraticket():
    url = "https://rahulkarthi0602.atlassian.net/rest/api/3/issue"

    API_TOKEN = "" #add jira api token 
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
