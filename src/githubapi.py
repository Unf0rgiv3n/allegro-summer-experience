import requests
import json

class GithubAPI():

    access_url = "https://api.github.com"
    version = "v3"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_user_repos(self, username):
        access_url = self.access_url
        endpoint = access_url + f'/users/{username}/repos'
        request = requests.get(endpoint)
        if request.status_code in range(200,299):
            return request.json()
        else:
            raise Exception("failed to request")
