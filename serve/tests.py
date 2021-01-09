import platform
import os

from django.test import TestCase

# Create your tests here.
sys_name = platform.system()
if sys_name == 'Windows':
    path = "D:\\"
    os.chdir(path)
    str1 = os.popen('netstat -ano')
    print(str1)