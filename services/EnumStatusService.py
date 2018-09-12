class EnumStatusService: 
    SERVICE_STOPPED = 1
    SERVICE_START_PENDING = 2
    SERVICE_STOP_PENDING = 3
    SERVICE_RUNNING = 4
    SERVICE_CONTINUE_PENDING = 5
    SERVICE_PAUSE_PENDING = 6
    SERVICE_PAUSED = 7

    @staticmethod
    def getStatus(status):
        
        if status == EnumStatusService.SERVICE_STOPPED:
            return 'STOPPED'
        elif status == EnumStatusService.SERVICE_START_PENDING:
            return 'START_PENDING'
        elif status == EnumStatusService.SERVICE_STOP_PENDING:
            return 'STOP_PENDING'
        elif status == EnumStatusService.SERVICE_RUNNING:
            return 'RUNNING'
        elif status == EnumStatusService.SERVICE_CONTINUE_PENDING:
            return 'CONTINUE_PENDING'
        elif status == EnumStatusService.SERVICE_PAUSE_PENDING:
            return 'PAUSE_PENDING'
        elif status == EnumStatusService.SERVICE_PAUSED:
            return 'PAUSED'
        