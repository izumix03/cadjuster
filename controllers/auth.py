import flask
import google_auth_oauthlib
import google_auth_oauthlib.flow
from flask import Blueprint

from controllers.sessions import set_credentials

auth_page = Blueprint("auth_page", __name__)


@auth_page.route("/auth", methods=["POST"])
def auth():
    # flask.session.permanent = True
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=[
            'https://www.googleapis.com/auth/calendar.calendarlist',
            'https://www.googleapis.com/auth/calendar.events.owned'
        ])
    flow.redirect_uri = 'http://localhost:5000/oauth2callback'
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        prompt='consent',  # 強制的に refresh token渡させる
        include_granted_scopes='true'
    )

    # TODO: store state in server database and verify in callback
    return flask.redirect(authorization_url)


@auth_page.route('/oauth2callback')
def oauth2callback():
    # TODO: store state in server database and verify in callback
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar.calendarlist',
                'https://www.googleapis.com/auth/calendar.events.owned'])
    flow.redirect_uri = flask.url_for('auth_page.oauth2callback', _external=True)

    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    set_credentials(flow.credentials)

    return flask.redirect(flask.url_for('daily_report_page.daily_report'))
