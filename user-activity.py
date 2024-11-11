import sys
import urllib.request
import urllib.error
import json

# This is the command line argument
arguments = sys.argv

# This is the username
username = arguments[1]

# This is the request to the API
request = urllib.request.Request(
    # This is the URL to the API
    url = 'https://api.github.com/users/'+ username+ '/events',
    # This is the headers to the API
    headers = {
        'User-Agent':'github-user-activity-cli',
        "Accept":'application/json'
    }
)
#This process is like receiving a package:
# Getting the package (urlopen)
# Opening the package (read)
# Translating the content to your language (decode)
# Organizing the content in a useful way (json.loads)
try:
    response = urllib.request.urlopen(request)
    response_data = response.read()
    response_string = response_data.decode('utf-8') 
    response_json = json.loads(response_string)
    
    # This is the loop to iterate through the response_json
    for event in response_json:
        #PushEvent
        if event["type"] == "PushEvent":
            name = event["repo"]["name"]
            commits = event["payload"]["size"]
            print(f"- Pushed {commits} commits to {name}")

        #PullRequestEvent
        if event["type"] == "PullRequestEvent":
            name = event["repo"]["name"]
            action = event["payload"]["action"]
            prtitle = event["payload"]["pull_request"]["title"]
            prnumber = event["payload"]["pull_request"]["number"]
            print(f"- {action} PR #{prnumber}: {prtitle}")

        #IssuesEvent
        if event["type"] == "IssuesEvent":
            repo_name = event["repo"]["name"]
            action = event["payload"]["action"]  # opened, closed, etc.
            issue_title = event["payload"]["issue"]["title"]
            issue_number = event["payload"]["issue"]["number"]
            print(f"- {action.capitalize()} issue #{issue_number}: '{issue_title}' in {repo_name}")

        #WatchEvent
        if event["type"] == "WatchEvent":
            repo_name = event["repo"]["name"]
            print(f"- Starred repository {repo_name}")

        #CreateEvent
        if event["type"] == "CreateEvent":
            repo_name = event["repo"]["name"]
            ref_type = event["payload"]["ref_type"]  # "branch" or "tag"
            ref = event["payload"]["ref"]  # name of branch/tag
            print(f"- Created {ref_type} '{ref}' in {repo_name}")

        #ForkEvent
        if event["type"] == "ForkEvent":
            repo_name = event["repo"]["name"]
            fork_name = event["payload"]["forkee"]["full_name"]
            print(f"- Forked {repo_name} to {fork_name}")

        #DeleteEvent
        if event["type"] == "DeleteEvent":
            repo_name = event["repo"]["name"]
            ref_type = event["payload"]["ref_type"]  # "branch" or "tag"
            ref = event["payload"]["ref"]  # name of branch/tag
            print(f"- Deleted {ref_type} '{ref}' in {repo_name}")
    
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(f"Error: Username not found")
    elif e.code == 403:
        print("Error: API rate limit exceeded")
    else:
        print(f"HTTP Error: {e.code} - {e.reason}")
        
except urllib.error.URLError as e:
    print(f"Network Error: Unable to connect to GitHub ({e.reason})")
    
except json.JSONDecodeError as e:
    print(f"Error: Invalid response from GitHub")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")











