import json
import platform
import os
import subprocess

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
    return HttpResponse(json.dumps(_list_data))


def add_serve(request):
    form_data = json.loads(request.body)
    serve_model = ServeModel()
    for field in form_data:
        serve_model.__setattr__(field, form_data[field])
    serve_model.save()
    return HttpResponse()


def get_serve(request):
    serve_id = get_param(request, 'id')
    sm: ServeModel = ServeModel.objects.get(id=serve_id)
    return HttpResponse(json.dumps(sm.to_serialize()))


# 获取请求参数
def get_param(request, key):
    form_data = json.loads(request.body)
    return form_data[key]


# 执行启动脚本
def start_serve(request):
    serve_id = get_param(request, 'id')
    sm = ServeModel.objects.get(id=serve_id)
    do_opera_serve(sm, 'stop')
    do_opera_serve(sm)


def do_opera_serve(serve_model: ServeModel, opera_mode='run'):
    sys_name = platform.system()
    if sys_name == 'Windows':
        path = serve_model.serve_path
        envs = os.environ
        envs['CATALINA_HOME'] = path
        proc = subprocess.Popen(path + 'catalina.bat ' + opera_mode, stderr=subprocess.STDOUT,
                                stdout=subprocess.PIPE, shell=True,
                                env=envs)
        out = proc.stdout
        for i in iter(out.readline, ''):
            if len(i) < 1:
                break
            print(i.decode('gbk').strip())
