import os
import json
import requests


class Helpers:

    def __init__(self) -> None:
        self.username = os.environ.get('GITHUB_USERNAME')
        self.token = os.environ.get('GITHUB_TOKEN')
        self.headers = {
            'Authorization': f'token {self.token}',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self._base_url = 'https://api.github.com/'
        self._url = None

    def __getattribute__(self, attr: str) -> object:
        """
        Usage: get all callable functions from the class and set the url based on the function name

        :param attr:
        :return:
        """
        attribute = object.__getattribute__(self, attr)

        class_name = object.__getattribute__(self, '__class__')
        allowedAttributes = [func for func in dir(class_name) if
                             callable(getattr(class_name, func)) and not any(x in func for x in ['__', 'help'])]

        if callable(attribute) and attr in allowedAttributes:
            def wrapper(*args, **kwargs):
                self.url = attr
                return attribute(*args, **kwargs)

            return wrapper
        return attribute

    @property
    def url(self) -> str:
        """
        Usage: get url of the current endpoint

        :return:
        """
        return self._url

    @url.setter
    def url(self, var: str) -> None:
        """
        Usage: set url to a specific endpoint based on the function name

        :param var:
        :return:
        """
        urls = {
            'help': 'help',
            'get_repos': 'search/repositories?q=user:',
            'make_repo': 'user/repos'
        }
        self._url = f'{self._base_url}{urls[var]}'

    @staticmethod
    def help(*args) -> str:
        """
        Usage: print out all available functions and their usage

        :param args:
        :return:
        """
        _ = args
        return """
        Usage: python main.py <function_name> <repo_name> <repo_visibility>
        Available functions:
            help: shows this message
            make_repo: creates a new repo
            get_repos: gets all repos from a user
        """

    def get_repos(self) -> list[dict[str, str]]:
        """
        Usage: python main.py get_repos

        :return:
        """
        data = requests.get(f'{self._url}{self.username}', headers=self.headers).json()
        return [{f"{data['items'][i]['name']}": f"{data['items'][i]['clone_url']}"} for i in range(len(data['items']))]

    def make_repo(self, *args) -> dict:
        """
        Usage: python main.py make_repo <repo_name> <repo_visibility>

        :param args:
        :return:
        """
        repo_name = args[0]
        visibility = args[1]
        repo_visibility = {
            'public': False,
            'private': True
        }
        repo_data = {
            "name": repo_name,
            "private": repo_visibility[visibility]
        }
        json_data = json.dumps(repo_data)

        response = requests.post(self.url, headers=self.headers, data=json_data)
        response = response.json()
        info = {
            'name': response['name'],
            'visibility': response['visibility'],
            'clone_url': response['clone_url']
        }
        return info
