from flask import Blueprint, render_template, flash, redirect, url_for, request
from iismonitorpy.services.Services import Services
import psutil, json

services_api = Blueprint('services_api', __name__, template_folder='templates')

@services_api.route("/all")
def getall(): 
    allServices = psutil.process_iter(attrs=['pid', 'name', 'username'])
    smarServices = []
    smarServices.append(getJOB('MySQL57'))
    return json.dumps([p.__dict__ for p in smarServices])


# methods
def getJOB(name = ""): 
    job = getServiceByName(name)
    if(job):
        # winService = psutil.win_service_get(job.)
        
        return Services(name, job.status(), job.start_type())
    else:
        return Services(name)

def getServiceByName(name = ""):
    #for p in psutil.process_iter(attrs=['pid', 'name', 'username']):
    for p in psutil.win_service_iter():
        if p.name() == name:
            return p
    return None
