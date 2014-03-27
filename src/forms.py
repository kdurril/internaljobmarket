"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators

from .models import ExampleModel


class ClassicExampleForm(wtf.Form):
    example_name = wtf.TextField('Name', validators=[validators.Required()])
    example_description = wtf.TextAreaField('Description', validators=[validators.Required()])


class StudentForm(wtf.Form):
    nameLast = TextField('Last Name', [validators.Length(min=2, max=25)])
    nameFirst = TextField('First Name', [validators.Length(min=1, max=25)])
    studentUid = TextField('Student UID', validators.Length(9)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    phone = TextField('Phone', [validators.Length(min=1, max=25)])
    major = TextField('Specialization', [validators.Length(min=1, max=25)])
    programCode = TextField('Program Code', [validators.Length(min=1, max=25)])
    semBegin = TextField('Beginning Semester', [validators.Length(min=1, max=25)])
    creditFall = TextField('Fall Credit', [validators.Length(min=1, max=25)])
    creditSpring = TextField('Spring Credit', [validators.Length(min=1, max=25)])
    request201408 = BooleanField('Fall Request', [validators.Required()])
    request201501 = BooleanField('Spring Request', [validators.Required()])
    
class SupervisorForm(wtf.Form):
    nameLast = TextField('Last Name', [validators.Length(min=2, max=25)])
    nameFirst = TextField('First Name', [validators.Length(min=1, max=25)])
    supervisor_id = TextField('Supervisor UID', validators.Length(min=1, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    room = TextField('Room')
    center = TextField('Center')
    
class PositionForm(wtf.Form):
    title = TextField('Title', [validators.Length(min=2, max=255)])
    workGroup = TextField('Center or Work Group')
    position_type = SelectField('Position Type',\
                                choices=[('GA', 'Graduate Assistant'),\
                                        ('AA', 'Administrative Assistant'),\
                                        ('RA', 'Research Assistant'),\
                                        ('TA', 'Teaching Assistant')])
    course = SelectField('Course',\
                            choices=[('PUAF610', 'PUAF610'),\
                                    ('PUAF611', 'PUAF611'),\
                                    ('PUAF620', 'PUAF620'),\
                                    ('PUAF640', 'PUAF640'),\
                                    ('PUAF641', 'PUAF641'),\
                                    ('PUAF670', 'PUAF670'),\
                                    ('PUAF781', 'PUAF781')])
    programMin = SelectField('Min Program Level',\
                            choices=[('M1', 'Masters 1st Year'),\
                                    ('M2', 'Masters 2nd Year'),\
                                    ('Phd1', 'PhD 1st Year'),\
                                    ('Phd2', 'PhD 2nd Year'),\
                                    ('PhdCadidate', 'PhD Candidate')])
    programStd = SelectField('Standard Program Level',\
                            choices=[('M1', 'Masters 1st Year'),\
                                    ('M2', 'Masters 2nd Year'),\
                                    ('Phd1', 'PhD 1st Year'),\
                                    ('Phd2', 'PhD 2nd Year'),\
                                    ('PhdCadidate', 'PhD Candidate')])
    positionOverview = TextAreaField('Position Overview', [validators.Length(min=2, max=255)])
    primaryDuties = TextAreaField('Primary Duties', [validators.Length(min=2, max=255)])
    necessarySkill = TextAreaField('Required Skills', [validators.Length(min=2, max=255)])
    preferredSkill = TextAreaField('Additional Skills', [validators.Length(min=2, max=255)])
    dateOpen = DateField('Open Date')
    dateClosed = DateField('Close Date')
    available = Integer('Available Positions', [validators.Required()])
    supervisor_id = TextField('Supervisor ID', [validators.Required()])

class ApplicationForm(wtf.Form):
    app_id = HiddenField()
    student_id = TextField('Student Directory ID')
    position_id = HiddenField('Student Directory ID')

class OfferForm(wtf.Form):
    offer_id = HiddenField()
    app_id = HiddenField()
    offerMade = RadioField('Offer', choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')])
    offer_date = DateField('Open Date')
    response RadioField('Offer', choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')])
    response_date = HiddenField()
    available = DateField('Date Available')