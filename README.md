
# Control GitHub with Batch  
  
## About  
Current version is able to get and create repositories.  
Future iterations will incorporate more features.  
  
## Functionality  
- Help
  - ```github help```
  - Return current functionality and usage.
- Make Repos
  - ```github make_repo <name> <visibility>```
    - visibility: public/private
  - Returns verification of repo creation.
- Get Repos
  - ```github get_repos```
  - Return a list of all current repos.
## Data
```python
 help = 'list of current functions and how to use them'
 make_repo = {'name': 'NAME', 'visibility': 'PRIVATE/PUBLIC', 'clone_url': 'https://github.com/USERNAME/REPO_NAME.git'}
 get_repos = [{'REPO_NAME': 'https://github.com/USERNAME/REPO_NAME.git'}, etc...]
```
## SETUP
### Installation
- Clone the repo: git clone https://github.com/Xisurthros/RepoCreationAutomation.git
- run `pip install requirements.txt`
### Authentication
- Create a personal access token with repo permissions.
- This can be done here: https://github.com/settings/tokens
- Set each os environment variable using the following commands in CMD:
  - Make sure to replace <USERNAME> and <TOKEN> with your own.
  - `setx GITHUB_USERNAME <USERNAME>`
  - `setx GITHUB_TOKEN <TOKEN>`
### Batch
- Replace the following in the github.bat file:
  - `SET PYTHON_PATH=PATH_TO_PYTHON`
  - `SET SCRIPT_PATH=PATH_TO_SCRIPT`
- Set path to github.bat in environment variables.
  - `SETX PATH "%PATH%;PATH_TO_GITHUB.BAT"`
  - Restart terminal.
  - Run `github help` to verify installation.
  