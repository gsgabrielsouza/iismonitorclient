from flask import Blueprint, render_template, flash, redirect, url_for, request
from iismonitorpy.monitor.HardDrive import HardDrive
import psutil, json

monitor_api = Blueprint('monitor_api', __name__, template_folder='templates')

@monitor_api.route("/cpu")
def getCPU():
    return json.dumps(psutil.cpu_percent())

@monitor_api.route("/memory")
def getMemory():
    return json.dumps(psutil.virtual_memory().percent)


@monitor_api.route("/diskpartitions")
def getDisk():
    dps = psutil.disk_partitions()

    hardDrives = []
    # hardDrives.append(fmt_str.format("Drive", "Type", "Opts"))
    for dp in dps:
        if dp.opts != 'cdrom' : 
            diskUsage = psutil.disk_usage(dp.device)
            # ((986498199552 /1024) / 1024 ) / 1024 
            #                           KB          MB      GB          
            totalGB = (((diskUsage.total / 1024) / 1024) / 1024)
            usedGb = (((diskUsage.used / 1024) / 1024) / 1024)
            freeGB  = totalGB - usedGb
            hd = HardDrive(dp.device, diskUsage.percent, totalGB, usedGb, freeGB)

           # hardDrives.append(fmt_str.format(dp.device, dp.fstype, dp.opts))
            hardDrives.append(hd)
    #return json.dumps(dps[0])
    return json.dumps([p.__dict__ for p in hardDrives]) 