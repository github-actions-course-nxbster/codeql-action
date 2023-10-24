from sarif import loader
import requests
import json
import sys
import json

#Set up API request headers
token = sys.argv[1] #${{ secrets.GITHUB_TOKEN }}
repository_name = sys.argv[2] #$GITHUB_REPOSITORY
workspace_location = sys.argv[3] #$GITHUB_WORKSPACE
ben_pat = sys.argv[4] #${{ secrets.BEN_PAT }}

#Set up API Request
headers = {"Authorization" : "token {}".format(token)}
pat_headers = {"Authorization" : "token {}".format(ben_pat)}
issue_api_url = "https://api.github.com/repos/{}/issues".format(repository_name)
jira_creation_url= "https://api.github.com/repos/{}/actions/workflows/jira-issue.yml/dispatches".format(repository_name)

#Get existing issues in repo
issues = []
response = requests.get(issue_api_url,headers=headers)

response_json = json.loads(response.content)
for issue in response_json:
    print(issue["body"])
    issues.append(issue["body"])
print(issues)

#Read in Sarif File
sarif_data = loader.load_sarif_file('../results/csharp.sarif')
record_data = sarif_data.get_records()

#Loop through identified vulnerabilities
for vulnerability in record_data:
    issue_title = vulnerability["Code"]
    issue_body = str(vulnerability["Tool"]) + str(vulnerability["Location"]) + str(vulnerability["Line"]) + str(vulnerability["Code"])
    
    if issue_body in issues:
        print("Duplicate identified")
    else:
        #Create GitHub Issues [Test]
        github_data = {"title": issue_title, "body": issue_body}
        create_issue = requests.post(issue_api_url,data=json.dumps(github_data),headers=headers)
        #issue_number = create_issue.content["number"]
        #Trigger Jira Action
        jira_data = {"ref": "master", "inputs": {"title": issue_title, "body": issue_body}}
        trigger_jira_action = requests.post(jira_creation_url,data=json.dumps(jira_data),headers=pat_headers)
        print(trigger_jira_action.content)
        print("Issue Created!")
