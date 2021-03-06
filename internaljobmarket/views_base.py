#GA Process 
#Views
#-*- coding: utf-8 -*-
#http://flask.pocoo.org/docs/views/ Method Based Dispatching

from internaljobmarket import app
from flask import render_template, redirect, url_for
from flask.views import MethodView
from internaljobmarket.models import StudentModel, SupervisorModel, PositionModel, ApplicationModel, OfferModel
from internaljobmarket.forms import StudentForm, SupervisorForm, PositionForm, ApplicationForm, OfferForm
from internaljobmarket.database import db_session


app.secret_key = ''

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bros/')
def student():
    "review student record"

    student = StudentModel()
    student = student.query.all()
    form = StudentForm()

    
    return render_template('student_review.html', student_list=student, form=form)

@app.route('/bros/<int:student_id>', methods=['GET','PUT'])
def student_by_id(student_id):
    student = StudentModel()
    #need an object and a list containing object for template
    student = student.query.get(student_id)
    current_student = student
    form = StudentForm(obj=student)
                        
    return render_template('student_update.html', student_id=student_id, student_list=[current_student], form=form)

class StudentTest(MethodView):
    def post(self, student_id=None):
        student = StudentModel()
        form = StudentForm()
        if student_id == None:
            if form.validate_on_submit():
                form.populate_obj(student)
                db_session.add(student)
                db_session.commit()
                return redirect('student_test')
        else:
            if form.validate_on_submit():
                student_by_id = student.query.get(student_id) 
                
                student_by_id.studentUid = form.studentUid.data
                student_by_id.nameLast = form.nameLast.data
                student_by_id.nameFirst = form.nameFirst.data
                student_by_id.email = form.email.data
                student_by_id.phone = form.phone.data
                student_by_id.major = form.major.data
                student_by_id.programCode = form.programCode.data
                student_by_id.semBegin = form.semBegin.data
                student_by_id.graduationExpected = form.graduationExpected.data
                student_by_id.creditFall = form.creditFall.data
                student_by_id.creditSpring = form.creditSpring.data 
                student_by_id.request201408 = form.request201408.data
                student_by_id.request201501 = form.request201501.data
                db_session.commit()
                return redirect('student_test')

        return redirect('/')

    def put(self, student_id):
        student = StudentModel()
        student_by_id = student.query.get(student_id)
        form = StudentForm()
        if form.validate_on_submit():
            form.populate_obj(student)
            db_session.update(student_by_id)
            db_session.commit()
            return redirect('student_test')
        return redirect('/')
        

    def delete(self, student_id):

        student = StudentModel()
        student_by_id = student.query.get(student_id)
        db_session.delete(student_by_id)
        db_session.commit()
        return redirect('student_test')
        
    def get(self, student_id=None):

        if student_id == None:
            student = StudentModel()
            student_list = student.query.all()
            form = StudentForm()
            return render_template('student_test.html', student_list=student_list, form=form)
        else:
            student = StudentModel()
            student_list = student.query.get(student_id)
            form = StudentForm(obj=student_list)
            return render_template('student_test_update.html', student_id=student_id, student_list=[student_list], form=form)

student_test = StudentTest.as_view('student_test')
student_put = StudentTest.as_view('student_put')

app.add_url_rule('/student_test/',\
    view_func=student_test,\
    methods=['GET','POST'])

app.add_url_rule('/student_test/<int:student_id>',\
    view_func=student_put,\
    methods=['GET', 'PUT', 'DELETE'])



class StudentView(MethodView):

    def post(self):
        "create new student record, http://flask.pocoo.org/snippets/63/ for easy WTforms redirect"
        student = StudentModel()
        form = StudentForm()
        if form.validate_on_submit():
            form.populate_obj(student)
            '''student = StudentModel(
            None,
            form.studentUid.data,
            form.nameLast.data,
            form.nameFirst.data,
            form.email.data,
            form.phone.data,
            form.major.data,
            form.programCode.data,
            form.semBegin.data,
            form.graduationExpected.data,
            form.creditFall.data,
            form.creditSpring.data, 
            form.request201408.data,
            form.request201501.data
                )'''
            db_session.add(student)
            db_session.commit()
            return redirect('/')
            
            
        return render_template('student_review.html', student_list=student, form=form)

    def put(self, student_id):
        "edit student record"
        "http://wtforms.simplecodes.com/docs/0.6.1/forms.html#wtforms.form.Form.populate_obj"
        student = StudentModel()
        student_update = student.query.get(student_id)
        current_student = [student_update]
        form = StudentForm()
        
        student_update.studentUid=form.studentUid.data
        student_update.nameLast=form.nameLast.data
        student_update.nameFirst=form.nameFirst.data
        student_update.email=form.email.data
        student_update.phone=form.phone.data
        student_update.major=form.major.data
        student_update.programCode=form.programCode.data
        student_update.semBegin=form.semBegin.data
        student_update.graduationExpected=form.graduationExpected.data
        student_update.creditFall=form.creditFall.data
        student_update.creditSpring=form.creditSpring.data 
        student_update.request201408=form.request201408.data
        student_update.request201501=form.request201501.data

        db_session.commit()

        if form.validate_on_submit():
            
            student_update.studentUid=form.studentUid.data
            student_update.nameLast=form.nameLast.data
            student_update.nameFirst=form.nameFirst.data
            student_update.email=form.email.data
            student_update.phone=form.phone.data
            student_update.major=form.major.data
            student_update.programCode=form.programCode.data
            student_update.semBegin=form.semBegin.data
            student_update.graduationExpected=form.graduationExpected.data
            student_update.creditFall=form.creditFall.data
            student_update.creditSpring=form.creditSpring.data 
            student_update.request201408=form.request201408.data
            student_update.request201501=form.request201501.data

            db_session.commit()
            return redirect('/')
        return redirect('/')
        #return render_template('student_update.html', student_id=student_id, student_list=current_update, form=form)


    def delete(self, student_id):
        "delete student record"
        student = StudentModel()
        student_delete = student.query.get(student_id)
        db_session.delete(student_delete)

        return redirect(url_for('student_view'))

    def get(self, student_id=None):
        "review student record"
        if student_id is None:
            student = StudentModel()
            student_list = student.query.all()
            form = StudentForm()
            
            return render_template('student_review.html', student_list=student_list, form=form)
        else:
            student = StudentModel()
            #need an object and a list containing object for template
            #

            student = student.query.get(student_id)
            current_student = student
            form = StudentForm(obj=student)
            #student.populate_obj(form)
            #form.studentUid.data = student.studentUid 
            #form.nameLast.data = student.nameLast
            #form.nameFirst.data = student.nameFirst
            #form.email.data = student.email
            #form.phone.data = student.phone 
            #form.major.data = student.major 
            #form.programCode.data = student.programCode 
            #form.semBegin.data = student.semBegin
            #form.graduationExpected.data = student.graduationExpected
            #form.creditFall.data = student.creditFall
            #form.creditSpring.data = student.creditSpring
            #form.request201408.data = student.request201408
            #form.request201501.data = student.request201501
                
            return render_template('student_update.html', student_id=student_id, student_list=[current_student], form=form)


        #return render_template('student_reveiw.html', students=students)
        

        #def show_user(username):
        #    student = StudentView.query.filter_by(student=username).first_or_404()
        #    return render_template('show_user.html', user=user)
        
        
#Move to urls
#app.add_url_rule('/students/', view_func=StudentView.as_view('students'),\
#    template_name='student_review.html', methods=['GET',])
#app.add_url_rule('/students/add', view_func=StudentView.as_view('students'),\
#    template_name='student_review.html', methods=['POST',])
#app.add_url_rule('/students/<int: student_id>', view_func=StudentView.as_view('students'),\
#    template_name='student_review.html', methods=['GET', 'PUT', 'DELETE'])


class SupervisorView(MethodView):
    def post(self):
        "create supervisor record"
        supervisor = SupervisorModel()
        form = SupervisorForm()
        if form.validate():
           supervisor(
           10,
           form.nameLast.data,
           form.nameFirst.data,
           form.phone.data,
           form.email.data,
           form.room.data,
           form.center.data
           )
           db_session.add(supervisor)
           db_session.commit()
        return redirect('/')
        

    def put(self, supervisor_id):
        "edit supervisor record"
        pass

    def delete(self, supervisor_id):
        "delete supervisor record"
        supervisor = SupervisorModel()
        supervisor = supervisor.delete(supervisor_id)
        pass

    def get(self):
        "review supervisor record"
        supervisor = SupervisorModel()
        supervisor = supervisor.query.all()
        form = SupervisorForm()
        #supervisor can only view his own record
        return render_template('supervisor_review.html', supervisor_list=supervisor, form=form)
#Move to urls
#app.add_url_rule('/supervisors/', view_func=SupervisorView.as_view('supervisors'), template_name='supervisor_review.html')

class PositionView(MethodView):

    def post(self):
        "create position record"
        position = PostionModel()
        form = PositionForm()
        if form.validate():
            position(
            form.position_id.data,
            form.title.data,
            form.workGroup.data,
            form.position_type.data,
            form.course.data,
            form.programMin.data,
            form.programStd.data,
            form.positionOverview.data,
            form.primaryDuties.data,
            form.necessarySkill.data,
            form.preferredSkill.data,
            form.dateOpen.data,
            form.dateClosed.data,
            form.available.data,
            form.supervisor_id.data
            )
            return position
            db_session.add(position)
            bd_session.commit()
        

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
#app.add_url_rule('/positions/', view_func=PositionView.as_view('positions'), template_name='position_review.html')
#this view must be restricted to the positon owner/supervisor
#app.add_url_rule('/positions/<int:position_id>', view_func=position_view,
#                 methods=['GET', 'PUT', 'DELETE'])

class ApplicationView(MethodView):
    def post(self, position_id):
        "create application record"
        applications = ApplicationModel()
        form = ApplicationForm(request.form)
        if form.validate():
            applications(form.app_id.data,
            form.student_id.data,
            form.position_id.data
            )
            return application
            db_session.add(application)
            db_session.commit()


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
#app.add_url_rule('/application/', view_func=ApplicationView.as_view('application'))

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

#app.add_url_rule('/offer/', view_func=OfferView.as_view('offer'), template_name='offer_review.html')
#app.add_url_rule('/offer/<int:offer_id>', view_func=offer_view,
#                 methods=['GET', 'PUT', 'DELETE'])

'''students.student_id = form.data.get('student_id')
            students.studentUid = form.data.get('studentUid')
            students.nameLast = form.data.get('nameLast')
            students.nameFirst = form.data.get('nameFirst')
            student.email = form.data.get('email')
            students.phone = form.data.get('phone')
            students.major = form.data.get('major')
            students.programCode = form.data.get('programCode')
            students.semBegin = form.data.get('semBegin')
            students.graudationExpected = form.data.get('graduationExpected')
            students.creditFall = form.data.get('creditFall')
            students.creditSpring = form.data.get('creditSpring')
            students.request201408 = form.data.get('request201408')
            students.request201501 = form.data.get('request201501')'''