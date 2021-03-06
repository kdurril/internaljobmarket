#GA Process 
#Views
#-*- coding: utf-8 -*-
#http://flask.pocoo.org/docs/views/ Method Based Dispatching

from internaljobmarket import app
from flask.views import MethodView
from flask.models import StudentModel, SupervisorModel, PositionModel, ApplicationModel, OfferModel
from flask.forms import StudentForm, SupervisorForm, PositionForm, ApplicationForm, OfferForm
import slqlite3

class StudentView(MethodView):

    def post(self):
        "create new student record"
        students = StudentModel()
        form = StudentForm(request.form)
        if form.validate():
            students.student_id = form.student_id.data
            students.studentUid. = form.studentUid.data
            students.nameLast = form.nameLast.data
            students.nameFirst = form.nameFirst.data
            student.email = form.email.data
            students.phone = form.phone.data
            students.major = form.major.data
            students.programCode = form.programCode.data
            students.semBegin = form.semBegin.data
            students.graudationExpected = form.graduationExpected.data
            students.creditFall = form.creditFall.data
            students.creditSpring = form.creditSpring.data
            students.request201408 = form.request201408.data
            students.request201501 = form.request201501.data
            return students
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

class SupervisorView(MethodView):
    def post(self):
        "create supervisor record"
        supervisors = SupervisorModel()
        form = SupervisorForm(request.form)
        if form.validate():
           supervisors.supervisor_id = form.supervisor_id.data
           supervisors.nameLast = form.nameLast.data
           supervisors.nameFirst = form.nameFirst.data
           supervisors.phone = form.phone.data
           supervisors.email = form.email.data
           supervisors.room = form.room.data
           supervisors.center =  form.center.data
           return supervisors
        pass

    def put(self, supervisor_id):
        "edit supervisor record"
        pass

    def delete(self, supervisor_id):
        "delete supervisor record"
        pass

    def get(self, supervisor_id):
        "review supervisor record"
        form = SupervisorForm()
        #supervisor can only view his own record
        pass
#Move to urls
app.add_url_rule('/supervisors/', view_func=Supervisors.as_view('supervisors'))

class PositionView(MethodView):

    def post(self):
        "create position record"
        positions = PostionModel()
        form = PositionForm(request.form)
        if form.validate():
            positions.position_id = form.position_id.data
            positions.title = form.title.data
            positions.workGroup = form.workGroup.data
            positions.position_type = form.position_type.data
            positions.course = form.course.data
            psoitions.programMin = form.programMin.data
            positions.programStd = form.programStd.data
            positions.positionOverview = form.positionOverview.data
            positions.primaryDuties = form.primaryDuties.data
            positions.necessarySkill = form.necessarySkill.data
            positions.preferredSkill = form.preferredSkill.data
            positions.dateOpen = form.dateOpen.data
            positions.dateClosed = form.dateClosed.data
            positions.available = form.available.data
            positions.supervisor_id = form.supervisor_id.data
        pass

    def put(self):
        "edit position record"
        pass

    def delete(self, position_id):
        "delete position record"
        pass

    def get(self):
        "review position record"
        form = PositionForm()
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

class ApplicationView(MethodView):
    def post(self, position_id):
        "create application record"
        applications = ApplicationModel()
        form = ApplicationForm(request.form)
        if form.validate():
            applications.app_id = form.app_id.data
            applications.student_id = form.student_id.data
            applications.postition_id = form.position_id.data
        pass

    def put(self, position_id):
        "edit application record"
        pass

    def delete(self, position_id):
        "delete application record"
        pass

    def get(self):
        "review application record"
        form = ApplicationForm()
        #if user is owner, decorate to allow put and delete
        if user_id is None:
            # return a list of users
            pass
        else:
            # expose a single user
            pass
        
#Move to urls
app.add_url_rule('/application/', view_func=Application.as_view('application'))

class OfferView(MethodView):
    def post(self, application_id):
        "create new offer"
        offers = OfferModel()
        form = OfferForm(request.form)
        if form.validate():
            offers.offer_id = form.offer_id.data
            offers.app_id = form.app_id.data
            offers.offerMade = form.offerMade.data 
            offers.offer_date = form.offer_date.data 
            offers.response = form.response.data
            offers.response_date = form.response_date.data
            offers.available = form.available.data
        pass

    def put(self, offer_id):
        "edit offer"
        pass

    def delete(self, offer_id):
        "delete offer"
        pass

    def get(self, offer_id):
        "review offer"
        form = OfferForm()
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