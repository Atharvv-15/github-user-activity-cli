# github-user-activity-cli
# GitHub User Activity CLI

A simple command-line tool that displays recent GitHub activity for any user.

## Description

This tool fetches and displays a user's recent GitHub activities, including:
- Push events
- Pull request activities
- Issue interactions
- Repository starring
- Branch/tag creation and deletion
- Repository forking

## Installation

1. Ensure you have Python 3.x installed on your system
2. Clone this repository:

bash
git clone [your-repository-url]

## Usage

Run the script from the command line by providing a GitHub username:

bash
python user-activity.py <username>


## Output Format

The tool displays activities in an easy-to-read format:

- Push events: `Pushed X commits to owner/repository`
- Pull requests: `[action] PR #X: [title]`
- Issues: `[Action] issue #X: '[title]' in owner/repository`
- Watch events: `Starred repository owner/repository`
- Create events: `Created [branch/tag] '[name]' in owner/repository`
- Fork events: `Forked owner/repository to new-owner/repository`
- Delete events: `Deleted [branch/tag] '[name]' in owner/repository`

## Error Handling

The script handles various error cases:
- Invalid username
- API rate limiting
- Network connectivity issues
- Invalid API responses

## Requirements

- Python 3.x
- Internet connection
- No additional packages required (uses standard library only)

## Limitations

- Subject to GitHub API rate limiting
- Shows only recent activities (as returned by the GitHub Events API)
- Requires public access to user's activity feed
