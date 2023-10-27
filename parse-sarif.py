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

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
GITHUB_REPOSITORY = os.environ['GITHUB_REPOSITORY']

#Set up Jira API Request
jiraOptions = {'server': JIRA_BASE_URL}
jira = JIRA(options=jiraOptions, basic_auth=( 
    JIRA_USER_EMAIL, JIRA_API_TOKEN)) 

#Get existing issues in Jira Project
issues = []
jql_str = 'project = {project}'.format(project = JIRA_PROJECT_NAME)
for singleIssue in jira.search_issues(jql_str=jql_str): 
    issues.append(singleIssue.fields)

#Set up GitHub security API Request
github_headers = {"Authorization" : "token {}".format(GITHUB_TOKEN)}
github_alerts_api_url = "https://api.github.com/repos/{}/code-scanning/alerts".format(GITHUB_REPOSITORY)

#Fetch GitHub repository alert data
alerts_response = requests.get(github_alerts_api_url, headers=github_headers)
alerts_response_json = json.loads(alerts_response.content)
print(alerts_response_json)

#Resolve open Jira issues that have have been addressed

#Add newly identified CodeQL alerts to Jira 

#Read in Sarif File
#sarif_data = loader.load_sarif_file('../results/csharp.sarif')
#print(sarif_data)
#record_data = sarif_data.get_records()

#vulnerability_count = 0
#issues_created = 0
#Loop through identified vulnerabilities
#for vulnerability in record_data:

    #vulnerability_count += 1
    #Create unique title for vulnerability
    #issue_title = vulnerability["Code"]
    #issue_body = str(vulnerability["Tool"]) + str(vulnerability["Location"]) + str(vulnerability["Line"]) + str(vulnerability["Code"])
    
    #Check if vulnerability already exists in Jira
    #if issue_body in issues:
        #Do not create dupicate issues in Jira
        #print("Duplicate identified")
    #else:
        #Create new issue in Jira
        #fields = {"project": { "key": JIRA_PROJECT_NAME }, "summary" : issue_body, "issuetype": { "name": "Task" }}
        #create_issue = jira.create_issue(fields=fields)
        #issues_created += 1
        #print("Issue Created!")

#Set output values summarizing scan results
#os.system("echo vulnerability_count={} >> $GITHUB_OUTPUT".format(vulnerability_count))
#os.system("echo issues_created={} >> $GITHUB_OUTPUT".format(issues_created))