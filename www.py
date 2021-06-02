from flask_debugtoolbar import DebugToolbarExtension

from application import app
from controllers.auth import auth_page
from controllers.daily_report import daily_report_page
from controllers.index import index_page

toolbar = DebugToolbarExtension(app)

app.register_blueprint(index_page)
app.register_blueprint(auth_page)
app.register_blueprint(daily_report_page)
