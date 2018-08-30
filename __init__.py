from flask import Flask, Blueprint, render_template

app = Flask(__name__)


from iismonitorpy.main.routes import home_api
from iismonitorpy.monitor.routes import monitor_api

app.register_blueprint(home_api, url_prefix='/')
app.register_blueprint(monitor_api, url_prefix='/monitor')
