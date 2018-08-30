from flask import Blueprint, render_template, flash, redirect, url_for, request
import psutil,json
monitor_api = Blueprint('monitor_api', __name__, template_folder='templates')



@monitor_api.route("/cpu")
def getCPU():
    
    return json.dumps(psutil.cpu_percent())