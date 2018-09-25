from flask_restful import Resource, reqparse, marshal_with, fields
import iismonitorclient.monitor.Service as appService 
import psutil, json

resource_fields = {
    'Partition': fields.String,
    'PercentUsed': fields.Float,
    'Used': fields.Float,
    'Free': fields.Float,
    'Total': fields.Float,
    'Slave': fields.Boolean,
}

class MemoryApi(Resource):
    def get(self):
        return appService.getMemoryPercent() 

class CpuApi(Resource):
    def get(self):
        return appService.getCPUPercent()

class HardDriveApi(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self):
        hardDrives = appService.getHardDrives()
        return hardDrives