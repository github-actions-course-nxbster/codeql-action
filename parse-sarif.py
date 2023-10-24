import os
from sarif import loader
import requests
import json
import sys
from jira import JIRA 

#Parse in required parameters
JIRA_BASE_URL = os.environ['JIRA_BASE_URL']
JIRA_USER_EMAIL = os.environ['JIRA_USER_EMAIL']
JIRA_API_TOKEN = os.environ['JIRA_API_TOKEN']
JIRA_PROJECT_NAME = os.environ['JIRA_PROJECT_NAME']

#Set up Jira API Request
jiraOptions = {'server': JIRA_BASE_URL}
jira = JIRA(options=jiraOptions, basic_auth=( 
    JIRA_USER_EMAIL, JIRA_API_TOKEN)) 

#Get existing issues in Jira Project
issues = []
jql_str = 'project = {project}'.format(project = JIRA_PROJECT_NAME)
for singleIssue in jira.search_issues(jql_str=jql_str): 
    issues.append(singleIssue.fields.summary)
    print('{}: {}:{}'.format(singleIssue.key, singleIssue.fields.summary, 
                             singleIssue.fields.reporter.displayName)) 

#TEST: Create Jira Issue
fields = {"project": { "key": JIRA_PROJECT_NAME }, "summary" : "Testing 123", "issuetype": { "name": "Task" }}
create_issue = jira.create_issue(fields=json.loads(fields))

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