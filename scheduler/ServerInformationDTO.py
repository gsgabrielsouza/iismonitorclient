from iismonitorpy.monitor.HardDriveDTO import HardDriveDTO

class ServerInformationDTO:
    MemoryPercent = 0.0
    CpuPercent = 0.0
    HardDrives = []

    def __init__(self, MemoryPercent, CpuPercent, hardDrives):
        self.MemoryPercent = MemoryPercent     
        self.CpuPercent = CpuPercent
        self.HardDrives = hardDrives
    
    def __repr__(self):
        info = f"Memory: {self.MemoryPercent}\nCPU: {self.CpuPercent}\nHD: "
        for item in self.HardDrives:
            info = info + item.Partition + " Free: " + str(item.Free)
        return  info