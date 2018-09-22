from iismonitorpy.services.EnumStatusService import EnumStatusService
from iismonitorpy.services.ServicesDTO import ServicesDTO
import psutil, win32serviceutil

# class Service:

def getJOBs(name = ""): 
    services = getServicesByName(name)
    if len(services) > 0:
        servicesdto = []
        for s in services:
            servicesdto.append(ServicesDTO(s.name(), s.status(), s.start_type()))
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