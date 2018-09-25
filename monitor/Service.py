from iismonitorclient.monitor.HardDriveDTO import HardDriveDTO
import psutil


def getMemoryPercent():
    return psutil.virtual_memory().percent

def getCPUPercent():
    return psutil.cpu_percent()

def getHardDrives():
    dps = psutil.disk_partitions()
    hardDrives = []
    for dp in dps:
        if dp.opts != 'cdrom' : 
            diskUsage = psutil.disk_usage(dp.device)
            #                           KB          MB      GB          
            totalGB = (((diskUsage.total / 1024) / 1024) / 1024)
            usedGb = (((diskUsage.used / 1024) / 1024) / 1024)
            freeGB  = totalGB - usedGb
            hd = HardDriveDTO(dp.device, diskUsage.percent, totalGB, usedGb, freeGB)

            hardDrives.append(hd)
    return hardDrives