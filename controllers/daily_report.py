import flask
import google
import googleapiclient
from flask import Blueprint, render_template
import google.oauth2.credentials
import googleapiclient.discovery
from models.calendar_service import CalendarService
from models.datex import Datex, Timezone
from controllers.sessions import set_credentials

daily_report_page = Blueprint("daily_report_page", __name__)


@daily_report_page.route("/daily_report")
def daily_report():
    if 'credentials' not in flask.session:
        return flask.redirect('auth')

    # Load credentials from the session.
    credentials = google.oauth2.credentials.Credentials(
        **flask.session['credentials']
    )

    set_credentials(credentials)

    service = CalendarService(googleapiclient.discovery.build('calendar', 'v3', credentials=credentials))

    today_events = service.active_events(
        Datex.create(Timezone.TOKYO).start().to_google_date(),
        Datex.create(Timezone.TOKYO).end().to_google_date(),
    )

    next_workday_events = service.active_events(
        Datex.create(Timezone.TOKYO).next_weekday().start().to_google_date(),
        Datex.create(Timezone.TOKYO).next_weekday().end().to_google_date(),
    )

    return render_template('daily_report.html',
                           title='日報用',
                           next_workday_titles=next_workday_events.titles(),
                           today_titles=today_events.titles())
