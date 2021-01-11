import platform
import os
import subprocess
import codecs

from django.test import TestCase

# Create your tests here.
sys_name = platform.system()
if sys_name == 'Windows':
    path = "D:\\coding\\testenv\\apache-tomcat-8.5.5-8032\\bin\\"
    os.chdir(path)
    # subprocess.run('echo 我是', stderr=subprocess.STDOUT, text=True, shell=True, encoding='utf-8')
    # os.system('catalina.bat run')
    envs = os.environ
    envs['CATALINA_HOME'] = 'D:\\coding\\testenv\\apache-tomcat-8.5.5-8032'
    proc = subprocess.Popen('ping www.baidu.com', stderr=subprocess.STDOUT,
                            stdout=subprocess.PIPE, shell=True,
                            env=envs)
    # outs = proc.communicate()
    out = proc.stdout
    for i in iter(out.readline, ''):
        if len(i) < 1:
            break
        print(i.decode('GBK').strip())
    # while True:
    #     content = out.readline()
    #     print(str(content))
