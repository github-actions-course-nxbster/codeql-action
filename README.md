# CodeQL Scan and Jira Issue Creation
Scan repository contents with CodeQL security and quality packs and create associated Issues in Jira for identified scanning findings

##Usage
```
name: Testing Composite Actions Workflow
steps:
  - uses: github-actions-course-nxbster/codeql-action@main
    with:
      language: ${{ matrix.language }}
      JIRA_BASE_URL: ${{ secrets.JIRA_BASE_URL }}
      JIRA_USER_EMAIL: ${{ secrets.JIRA_USER_EMAIL }}
      JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
      JIRA_PROJECT_NAME: 'AT'
```

##Action Spec:
###Environment Variables:
- None

###Inputs:
