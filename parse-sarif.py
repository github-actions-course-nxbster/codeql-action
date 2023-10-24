import os
from sarif import loader
import requests
import json
import sys

#Parse in request parameters
print(os.environ['Greeting'])

#Get existing issues in Jira Project
#issues = []
#response = requests.get(issue_api_url,headers=headers)

#Read in Sarif File
#sarif_data = loader.load_sarif_file('../results/csharp.sarif')
#record_data = sarif_data.get_records()

#Loop through identified vulnerabilities
#for vulnerability in record_data:

    #Create unique title for vulnerability
    #issue_title = vulnerability["Code"]
    #issue_body = str(vulnerability["Tool"]) + str(vulnerability["Location"]) + str(vulnerability["Line"]) + str(vulnerability["Code"])
    
    #Check if vulnerability already exists in Jira
    #if issue_body in issues:
        #Do not create dupicate issues in Jira
        #print("Duplicate identified")
    #else:
        #Create new issue in Jira
        #jira_data = {"ref": "master", "inputs": {"title": issue_title, "body": issue_body}}
        #trigger_jira_action = requests.post(jira_creation_url,data=json.dumps(jira_data),headers=pat_headers)
        #print("Issue Created!")