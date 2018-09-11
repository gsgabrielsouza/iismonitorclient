class HardDrive:
    Partition = ""
    PercentUsed  = 0
    Used = 0
    Free = 0
    Total = 0
    Slave = False

    def __init__(self, partition, percentUsed, total, used, free):
        self.Partition = partition
        self.PercentUsed = percentUsed
        self.Total = total
        self.Used = used
        self.Free = free