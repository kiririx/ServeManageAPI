import platform
import os
import subprocess
import codecs
import socket

from django.test import TestCase
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sk.connect(('127.0.0.1', 8080))
except OSError:
    print('not open')
