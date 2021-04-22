import os

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
            
        
        return render_template('index.html')


    return app
