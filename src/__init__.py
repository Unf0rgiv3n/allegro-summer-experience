import os
from .githubapi import GithubAPI

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

    @app.route('/home', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            username = request.form['github_name']
            github = GithubAPI()
            json_response = github.get_user_repos(username)
            repos_list = []
            stargazer_sum = 0
            for response in json_response:
                repos_list.append((response['name'], response['stargazers_count']))
                stargazer_sum += response['stargazers_count']    
            return render_template('index.html', content=repos_list, stars_sum=stargazer_sum)
        
        return render_template('empty_index.html')


    return app
