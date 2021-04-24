import os
from .githubapi import GithubAPI
#from .tokenConf import *

from flask import Flask, redirect, url_for, render_template, request

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except  OSError:
        pass

    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            username = request.form['github_name']
            github = GithubAPI()
            try:
                pages_max = github.get_repo_pages_number(username)
            except:
                return render_template('error.html')

            repos_list = []
            stargazer_sum = 0
            for page in range(pages_max):
                try:
                    json_response = github.get_user_repos(username, page+1)
                except:
                    return render_template('error.html')
                for response in json_response:
                    repos_list.append((response['name'], response['stargazers_count']))
                    stargazer_sum += response['stargazers_count']    
            return render_template('index.html', user=username, content=repos_list, stars_sum=stargazer_sum)
        
        return render_template('empty_index.html')


    return app
