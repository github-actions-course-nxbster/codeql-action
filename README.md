# CodeQL Scan and Jira Issue Creation
Scan repository contents with CodeQL security and quality packs and create associated Issues in Jira for identified scanning findings

## Usage
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

## Action Spec:
### Environment Variables:
- None

### Inputs:
- `language` (required) - List of languages to be scanned with CodeQL
- `JIRA_BASE_URL` (required) - Base URL of the Jira project used to create issues
- `JIRA_USER_EMAIL` (required) - Email of the user creating Jira issues
- `JIRA_API_TOKEN` (required) - API Access token required for querying the Jira API
- `JIRA_PROJECT_NAME` (required) - Jira project destination for created issued

### Outputs:
- None
