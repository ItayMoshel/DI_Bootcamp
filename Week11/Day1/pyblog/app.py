import flask
from flask import render_template_string, Flask, render_template

app = flask.Flask(__name__)

users = ["name1", "name2", "name3"]
articles = ["article1", "article2", "article3"]


@app.route("/")
def home():
    template_string = '''
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Hello, {{ string }}</h1>
        </body>
    </html>
    '''
    html = flask.render_template_string(template_string, string="somthing")
    return html


@app.route('/home/<username>')
def index(username):
    template_string = '''
        <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1>Hello, {{ name }}! How are you ?</h1>
            </body>
        </html>
    '''
    html = flask.render_template_string(template_string, name=username)
    return html


@app.route("/blog")
def welcome_users():
    template_string = '''
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            {% for user in users %}
            <h1>Hello, {{ user }}</h1>
            {% endfor %}
        </body>
    </html>
    '''
    html = flask.render_template_string(template_string, users=users)
    return html


@app.route("/blog/articles")
def article_display():
    template_string = '''
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            {% for article in articles %}
            <h1>Hello, {{ article }}</h1>
            {% endfor %}
        </body>
    </html>
    '''
    html = flask.render_template_string(template_string, articles=articles)
    return html


if __name__ == "__main__":
    app.run(debug=True)
