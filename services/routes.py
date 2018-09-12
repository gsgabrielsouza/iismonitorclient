from flask import Blueprint, render_template, flash, redirect, url_for, request
from iismonitorpy.services.Services import Services
from iismonitorpy.services.EnumStatusService import EnumStatusService
import psutil, json, win32serviceutil

services_api = Blueprint('services_api', __name__, template_folder='templates')

@services_api.route("/all")
def getall(): 
    allServices = psutil.process_iter(attrs=['pid', 'name', 'username'])
    smarServices = []
    smarServices = getJOBs('todo')
    return json.dumps([p.__dict__ for p in smarServices])

@services_api.route("/action")
def restart():
    service = request.args.get('n')
    action = request.args.get('action')
    return str(service_control(service, action))

# methods
def getJOBs(name = ""): 
    services = getServicesByName(name)
    if len(services) > 0:
        servicesdto = []
        for s in services:
            servicesdto.append(Services(s.name(), s.status(), s.start_type()))
        return servicesdto
    else:
        return []

def getServicesByName(name = ""):
    services = []
    for p in psutil.win_service_iter():
        if name in p.name() :
            services.append(p)
    return services

def service_control(service, action):
    try:
        if action == 'stop':
            win32serviceutil.StopService(service)
            return EnumStatusService.getStatus(win32serviceutil.QueryServiceStatus(service)[1])
        elif action == 'start':
            win32serviceutil.StartService(service)
            return EnumStatusService.getStatus(win32serviceutil.QueryServiceStatus(service)[1])
        elif action == 'restart':
            win32serviceutil.RestartService(service)
            return EnumStatusService.getStatus(win32serviceutil.QueryServiceStatus(service)[1])
        elif action == 'status':
            return EnumStatusService.getStatus(win32serviceutil.QueryServiceStatus(service)[1])
    except:
        return 'failed'