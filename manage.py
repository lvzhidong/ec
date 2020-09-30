#coding: u8

from flask_script import Manager
from application import create_app
from application.models import *

manager = Manager(create_app())

if __name__ == '__main__':
    import sys
    manager.run()
