#GA Process 
#Views
#-*- coding: utf-8 -*-
#http://flask.pocoo.org/docs/views/ Method Based Dispatching

from flask.views import MethodView
import slqlite3

class Student(MethodView):

    def post(self):
        "create new student record"
        pass

    def put(self, student_id):
        "edit student record"
        pass

    def delete(self, student_id):
        "delete student record"
        pass

    def get(self):
        "review student record"
        pass
#Move to urls
app.add_url_rule('/students/', view_func=Student.as_view('students'))

class Supervisor(MethodView):
    def post(self):
        "create supervisor record"
        pass

    def put(self, supervisor_id):
        "edit supervisor record"
        pass

    def delete(self, supervisor_id):
        "delete supervisor record"
        pass

    def get(self, supervisor_id):
        "review supervisor record"
        #supervisor can only view his own record
        pass
#Move to urls
app.add_url_rule('/supervisors/', view_func=Supervisors.as_view('supervisors'))

class Position(MethodView):

    def post(self):
        "create position record"
        pass

    def put(self):
        "edit position record"
        pass

    def delete(self, position_id):
        "delete position record"
        pass

    def get(self):
        "review position record"
        #if user is owner, decorate to allow put and delete
        if user_id is None:
            # return a list of users
            pass
        else:
            # expose a single user
            pass

#Move to urls
app.add_url_rule('/positions/', view_func=Positions.as_view('positions'))
#this view must be restricted to the positon owner/supervisor
app.add_url_rule('/positions/<int:position_id>', view_func=position_view,
                 methods=['GET', 'PUT', 'DELETE'])

class Application(MethodView):
    def post(self, position_id):
        "create application record"
        pass

    def put(self, position_id):
        "edit application record"
        pass

    def delete(self, position_id):
        "delete application record"
        pass

    def get(self):
        "review application record"
        #if user is owner, decorate to allow put and delete
        if user_id is None:
            # return a list of users
            pass
        else:
            # expose a single user
            pass
        
#Move to urls
app.add_url_rule('/application/', view_func=Application.as_view('application'))

class Offer(MethodView):
    def post(self, application_id):
        "create new offer"
        pass

    def put(self, offer_id):
        "edit offer"
        pass

    def delete(self, offer_id):
        "delete offer"
        pass

    def get(self, offer_id):
        "review offer"
        #if user is owner, decorate to allow put and delete
        if offer_id is owner:
            # return a list of users
            pass
        #if user is applicant offered position, allow view of its offers
        elif offer_id is applicant:
            pass
        else:
            # expose a single user
            pass
        
#Move to urls

app.add_url_rule('/offer/', view_func=Offer.as_view('offer'))
app.add_url_rule('/offer/<int:offer_id>', view_func=offer_view,
                 methods=['GET', 'PUT', 'DELETE'])