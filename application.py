import flask

from flask import render_template

application = flask.Flask(__name__)

@application.route('/oauth/authorize/')
def auth():
    " Render the app 'allowance' page. "
    return render_template('auth.html')

if __name__ == '__main__':
    application.run()