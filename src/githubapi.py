import requests
import json

class GithubAPI():

    access_url = "https://api.github.com"
    version = "v3"
    token=None
    headers=None
    #max 100 according to github api
    repos_per_page = 100
    
    def __init__(self, token=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if token is not None:
            self.token = token
            self.headers = {'Authorization': 'token ' + token}

    def get_user_repos(self, username, sort_option ,pagination_number=None):
        access_url = self.access_url
        endpoint = access_url + f'/users/{username}/repos?per_page={self.repos_per_page}'
        endpoint = endpoint + f'&sort={sort_option}'
        if pagination_number is not None:
            endpoint = endpoint + f'&page={pagination_number}'
        if  self.token is not None:
            request = requests.get(endpoint, headers=self.headers)
        else:
            request = requests.get(endpoint)
        if request.status_code in range(200,299):
            return request.json()
        else:
            raise Exception("failed to request")

    def get_repo_pages_number(self, username):
        access_url = self.access_url
        endpoint = access_url + f'/users/{username}/repos?per_page={self.repos_per_page}'
        request = requests.get(endpoint)
        if request.status_code in range(200,299):
            if 'link' in request.headers:
                links = request.headers['link']
                links_arr = links.split(';')
                #we are taking second from last cus there is coded a max number of pages
                #[' rel', '"next", <https://api.github.com/user/562236/repos?per_page', '50&page', '2>']
                number_of_pages = links_arr[-2].split('=')[-1].split('>')[0]
                return int(number_of_pages)
            else:
                return 1
        else:
            raise Exception("failed to request")