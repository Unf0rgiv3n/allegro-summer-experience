import requests
import json

class GithubAPI():

    access_url = 'https://api.github.com'
    headers = None
    version = 'v3'