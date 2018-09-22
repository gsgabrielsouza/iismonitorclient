from flask_restful import Resource, reqparse, marshal_with, fields
from flask import request
from iismonitorpy.services.ServicesDTO import ServicesDTO
import iismonitorpy.services.Service as appService 
import psutil, json, win32serviceutil

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to charge for this resource')

class WindowsServicesListApi(Resource):
    def get(self):
        allServices = psutil.process_iter(attrs=['pid', 'name', 'username'])
        services = []
        services = appService.getJOBs('todo')
        return services

class WindowsServiceAction(Resource):
    def get(self, name, action = ""):
        status = appService.service_control(name, action)
        if status != 'failed':
            return {'status': status}, 201
        else:
            return {'status': 'failed'}, 404
