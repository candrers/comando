#!/home/carlos/comando/env/bin/python
import wsgiref.handlers

from controle.wsgi import application

wsgiref.handlers.CGIHandler().run(application)
