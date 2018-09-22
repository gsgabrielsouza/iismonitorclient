class ServicesDTO:
    name = ""
    status = ""
    startType = ""
    
    def __init__(self, name, status = "not find", startType = ""):
        self.name = name
        self.status = status
        self.startType = startType