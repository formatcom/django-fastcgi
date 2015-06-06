#!/usr/bin/python
import os, sys

sys.path.insert(0, '/home/username/django/modules')
sys.path.insert(0, '/home/username/django/project')

os.environ['DJANGO_SETTINGS_MODULE'] = "project.settings"
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", deamonize="false")