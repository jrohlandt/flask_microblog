from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'jeandre'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Welcome to 2019, the future is here!'
        },
        {
            'author': {'username': 'Jane'},
            'body': 'Indeed, no flying cars but driveless cars are better anyway.'
        },
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)