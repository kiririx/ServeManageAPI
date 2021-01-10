import platform
import os
import subprocess
import codecs

from django.test import TestCase

# Create your tests here.
sys_name = platform.system()
if sys_name == 'Windows':
    path = "D:\\coding\\apache-tomcat-8.5.5\\bin\\"
    os.chdir(path)
    # subprocess.run('echo 我是', stderr=subprocess.STDOUT, text=True, shell=True, encoding='utf-8')
    # os.system('catalina.bat run')
    envs = os.environ
    envs['CATALINA_HOME'] = 'D:\\coding\\apache-tomcat-8.5.5'
    proc = subprocess.Popen(path + 'catalina.bat stop', stderr=subprocess.STDOUT,
                            stdout=subprocess.PIPE,shell=True,
                            env=envs)
    # outs = proc.communicate()
    out = proc.stdout
    for i in iter(out.readline, ''):
        if len(i) < 1:
            break
        print(i.decode('gbk').strip())
    # while True:
    #     content = out.readline()
    #     print(str(content))
