#GA Process 
#Views
#-*- coding: utf-8 -*-
#http://flask.pocoo.org/docs/views/ Method Based Dispatching

from flask.views import MethodView

class Student(MethodView):

    def post():
        "create new student record"
        pass

    def put():
        "edit student record"
        pass

    def delete():
        "delete student record"
        pass

    def get():
        "review student record"
        pass

class Supervisor(MethodView):
    def post():
        "create supervisor record"
        pass

    def put():
        "edit supervisor record"
        pass

    def delete():
        "delete supervisor record"
        pass

    def get():
        "review supervisor record"
        pass

class Position(MethodView):

    def post():
        "create position record"
        pass

    def put():
        "edit position record"
        pass

    def delete():
        "delete position record"
        pass

    def get():
        "review position record"
        pass

class Application(MethodView):
    def post():
        "create application record"
        pass

    def put():
        "edit application record"
        pass

    def delete():
        "delete application record"
        pass

    def get():
        "review application record"
        pass

class Offer(MethodView):
    def post():
        "create new offer"
        pass

    def put():
        "edit offer"
        pass

    def delete():
        "delete offer"
        pass

    def get():
        "review offer"
        pass