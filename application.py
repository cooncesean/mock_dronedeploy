import flask

from flask import render_template

application = flask.Flask(__name__)

@application.route('/oauth/authorize/')
def auth():
    " Render the app 'allowance' page. "
    return render_template('auth.html')

# https://api.instagram.com/oauth/authorize/?client_id=2e7067c2b22a4cbdb6b2e0e89cbd6537&response_type=code&redirect_uri=http://data.ink361.com/v1/auth?instagram=1

if __name__ == '__main__':
    application.run()