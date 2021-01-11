from enum import Enum


class Platform(Enum):
    WINDOWS = 'Windows'
    LINUX = 'Linux'
    MAC = 'Mac OS X'


class ServeAction(Enum):
    RUN = 'run'
    STOP = 'stop'
