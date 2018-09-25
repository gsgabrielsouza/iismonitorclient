from .ServerInformationDTO import ServerInformationDTO
import iismonitorclient.monitor.Service as appService 

class schedulerJob:
    @staticmethod
    def startJob():
        memoryPercent = appService.getMemoryPercent()
        cpuPercent = appService.getCPUPercent()
        hds = appService.getHardDrives()
        srvvInfo = ServerInformationDTO(memoryPercent, cpuPercent, hds)
        print(srvvInfo)
        # TODO: save infos