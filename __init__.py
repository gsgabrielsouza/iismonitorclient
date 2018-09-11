from flask import Flask, Blueprint, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import time

app = Flask(__name__)


from iismonitorpy.main.routes import home_api
from iismonitorpy.monitor.routes import monitor_api
from iismonitorpy.services.routes import services_api

app.register_blueprint(home_api, url_prefix='/')
app.register_blueprint(monitor_api, url_prefix='/monitor')
app.register_blueprint(services_api, url_prefix='/services')

# scheduler = BackgroundScheduler()
# job = scheduler.add_job(teste, 'interval', seconds=1)
# scheduler.start()
