from iismonitorpy.scheduler.ServerInformationDTO import ServerInformationDTO
import iismonitorpy.monitor.Service as appService 

class schedulerJob:
    @staticmethod
    def startJob():
        memoryPercent = appService.getMemoryPercent()
        cpuPercent = appService.getCPUPercent()
        hds = appService.getHardDrives()
        srvvInfo = ServerInformationDTO(memoryPercent, cpuPercent, hds)
        # TODO: save infos