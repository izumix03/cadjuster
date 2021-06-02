import os

from flask import Flask
from flask_script import Manager
app = Flask(__name__)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

manager = Manager(app)
app.config.from_pyfile("config/base_setting.py")

# linux export ops_config=local|production
# windows set ops_config=local|production
if "environment" in os.environ:
    app.config.from_pyfile("config/%s_setting.py" % (os.environ['environment']))
