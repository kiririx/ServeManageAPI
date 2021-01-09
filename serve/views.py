import json
import platform
import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from serve.models import ServeModel


def connect_token(request):
    return HttpResponse()


def list_data(request):
    objs = ServeModel.objects.all()
    _list_data = []
    for obj in objs:
        _list_data.append(obj.to_serialize())
    print(_list_data)
    return HttpResponse(json.dumps(_list_data))


def add_serve(request):
    form_data = json.loads(request.body)
    serve_model = ServeModel()
    for field in form_data:
        serve_model.__setattr__(field, form_data[field])
    serve_model.save()
    return HttpResponse()

# 执行启动脚本
def start_serve(request):
    sys_name = platform.system()
    if sys_name == 'Windows':
        path = "D:\\"
        os.chdir(path)
        os.execl('calc')
