from flask import Flask, Blueprint, render_template
from flask_restful import Api, Resource, url_for
from apscheduler.schedulers.background import BackgroundScheduler
from iismonitorpy.scheduler.schedulerJob import schedulerJob
from iismonitorpy.monitor.api import CpuApi, MemoryApi, HardDriveApi
from iismonitorpy.services.api import WindowsServicesListApi, WindowsServiceAction

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

from iismonitorpy.main.routes import home_api
from iismonitorpy.monitor.api import CpuApi, MemoryApi, HardDriveApi
from iismonitorpy.services.api import WindowsServiceAction, WindowsServicesListApi

api.add_resource(CpuApi, '/monitor/cpu')
api.add_resource(MemoryApi, '/monitor/memory')
api.add_resource(HardDriveApi, '/monitor/harddrive')

api.add_resource(WindowsServicesListApi, '/service/all')
api.add_resource(WindowsServiceAction, '/service/<string:name>/<string:action>')

app.register_blueprint(api_bp)


scheduler = BackgroundScheduler()
job = scheduler.add_job(schedulerJob.startJob, 'interval', seconds=5)
scheduler.start()
