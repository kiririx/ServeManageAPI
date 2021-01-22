from enum import Enum


# 平台
class Platform(Enum):
    WINDOWS = 'Windows'
    LINUX = 'Linux'
    MAC = 'Mac OS X'


# 服务启动命令
class ServeAction(Enum):
    RUN = 'run'
    STOP = 'stop'


# Web容器
class WebContainer(Enum):
    Tomcat = 'tomcat'
    Jetty = 'jetty'
