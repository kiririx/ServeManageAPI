import json
import platform
import os
import subprocess

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ServeManageAPI.env import Platform, ServeAction
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
        if field != 'id':
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
    do_opera_serve(sm, ServeAction.STOP)
    do_opera_serve(sm)
    return HttpResponse()


# 执行停止服务脚本
def stop_serve(request):
    serve_id = get_param(request, 'id')
    sm = ServeModel.objects.get(id=serve_id)
    do_opera_serve(sm, ServeAction.STOP)
    return HttpResponse()


def do_opera_serve(serve_model: ServeModel, opera_mode=ServeAction.RUN):
    sys_name = platform.system()
    if sys_name == Platform.WINDOWS.value:
        path = serve_model.serve_path
        envs = os.environ
        envs['CATALINA_HOME'] = path
        proc = subprocess.Popen(path + '\\bin\\catalina.bat ' + opera_mode.value, stderr=subprocess.STDOUT,
                                stdout=subprocess.PIPE, shell=True,
                                env=envs)
        out = proc.stdout
        output_content = ''
        for line_v in iter(out.readline, ''):
            if len(line_v) < 1:
                break
            line_str = line_v.decode('gbk').strip()
            output_content.join(line_str)
            print(line_str)

