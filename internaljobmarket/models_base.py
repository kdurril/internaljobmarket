from sqlalchemy import Column, Integer, String, ForeignKey, Table, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship

from internaljobmarket.database import Base


roleplay = '''
class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    users = relationship("User", backref="role")
    def __init__(self, name=None, users=None):
        self.name = name
        self.users = users

    def __repr__(self):
        return 'Role {0}'.format(self.name)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"))

    def __init__(self, username=None, role_id=None):
        self.username=username
        self.role_id=role_id

    def __repr__(self):
        return 'User {0}'.format(self.name)
'''

class StudentModel(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True)
    studentUid = Column(String(9), unique=True)
    nameLast = Column(String(120))
    nameFirst  = Column(String(120))
    email  = Column(String(120))
    phone  = Column(String(120))
    major  = Column(String(120))
    programCode  = Column(String(120))
    semBegin  = Column(String(120))
    graduationExpected  = Column(String(120))
    creditFall  = Column(Integer)
    creditSpring =  Column(Integer)
    request201408 = Column(String(120))
    request201501 = Column(String(120))
    position = relationship("ApplicationModel", backref='StudentModel')
    

    def __init__(self, student_id=None,
                studentUid=None, nameLast=None,
                nameFirst=None, email=None,
                phone=None, major=None,
                programCode=None, semBegin=None,
                graduationExpected=None, creditFall=None,
                creditSpring=None, request201408=None,
                request201501=None):
        self.student_id = student_id
        self.studentUid =  studentUid
        self.nameLast = nameLast
        self.nameFirst = nameFirst
        self.email = email
        self.phone = phone
        self.major = major
        self.programCode = programCode
        self.semBegin = semBegin
        self.graduationExpected = graduationExpected
        self.creditFall = creditFall
        self.creditSpring = creditSpring
        self.request201408 = request201408
        self.request201501 = request201501

    def __repr__(self):
        return '<Student {0}>'.format(self.studentUid)

class SupervisorModel(Base):
    __tablename__ = 'supervisor'
    supervisor_id = Column(Integer, primary_key=True)
    nameLast = Column(String(120))
    nameFirst = Column(String(120))
    phone = Column(String(120))
    email = Column(String(120))
    room = Column(String(120))
    center = Column(String(120))
    position = relationship("PositionModel", backref='SupervisorModel')
    

    def __init__(self, supervisor_id=None, 
                nameLast=None, nameFirst=None,
                phone=None, email=None,
                room=None, center=None
                ):
        self.supervisor_id = supervisor_id
        self.nameLast = nameLast
        self.nameFirst = nameFirst
        self.phone = phone
        self.email = email
        self.room = room
        self.center = center

    def __repr__(self):
        return '<Supervisor {0}>'.format(self.supervisor_id)

class PositionModel(Base):
    __tablename__ = 'position'
    position_id  = Column(Integer, primary_key=True)
    title = Column(String(120))
    workGroup = Column(String(120))
    position_type = Column(String(120))
    course = Column(String(120))
    programMin = Column(String(120))
    programStd = Column(String(120))
    positionOverview = Column(String(120))
    primaryDuties = Column(String(120))
    necessarySkill = Column(String(120))
    preferredSkill = Column(String(120))
    dateOpen = Column(String(120))
    dateClosed = Column(String(120))
    available = Column(String(120))
    supervisor_id = Column(Integer, ForeignKey("supervisor.supervisor_id"), nullable=False)
    supervisor = relationship("ApplicationModel", backref='PositionModel')
    superv = relationship("SupervisorModel", primaryjoin=supervisor_id == SupervisorModel.supervisor_id, viewonly=True)
    #application = relationship("application", backref='position')
    

    def __init__(self, position_id=None,
                title=None, workGroup=None, position_type=None,
                course=None, programMin=None, programStd=None,
                positionOverview=None, primaryDuties=None,
                necessarySkill=None, preferredSkill=None,
                dateOpen=None, dateClosed=None,
                available=None, supervisor_id=None):
        self.position_id = position_id
        self.title = title
        self.workGroup =workGroup
        self.position_type = position_type
        self.course = course
        self.programMin = programMin
        self.programStd = programStd
        self.positionOverview = positionOverview
        self.primaryDuties = primaryDuties
        self.necessarySkill = necessarySkill
        self.preferredSkill = preferredSkill
        self.dateOpen = dateOpen
        self.dateClosed = dateClosed
        self.available = available
        self.supervisor_id = supervisor_id

    def __repr__(self):
        return '<Position {0}>'.format(self.position_id)

class ApplicationModel(Base):
    'Many-to-many association table'
    __tablename__ = 'app_main'
    app_id = Column(Integer, primary_key=True)
    position_id = Column(Integer, ForeignKey('position.position_id'), nullable=False)
    student_id = Column(Integer, ForeignKey('student.student_id'), nullable=False)
    student = relationship('StudentModel',primaryjoin=student_id == StudentModel.student_id)
    offer = relationship('OfferModel', backref='AppilicationModel')
    UniqueConstraint('position_id', 'student_id', name='unique_app')
    

    def __init__(self, app_id=None,
                student_id=None,
                position_id=None):
        self.app_id = app_id
        self.position_id = position_id
        self.student_id = student_id

    def __repr__(self):
        return '<Application {0}'.format(self.app_id)

class OfferModel(Base):
    "This is a one-to-one from Application w/ Y or N"
    #This can rely on the application id completely
    __tablename__ =  'offer'
    offer_id = Column(Integer, primary_key=True)
    app_id = Column(Integer, ForeignKey('app_main.app_id'), nullable=False)
    offerMade = Column(String(120))
    offer_date = Column(String(120))
    response = Column(String(120))
    response_date = Column(String(120))
    available = Column(String(120))
    application = relationship('ApplicationModel',primaryjoin=app_id == ApplicationModel.app_id)
    

    def __init__(self, offer_id=None, app_id=None,
                offerMade=None, offer_date=None,
                response=None, response_date=None,
                available=None):
        self.offer_id = offer_id
        self.app_id = app_id
        self.offerMade = offerMade
        self.offer_date = offer_date
        self.response = response
        self.response_date = response_date
        self.available = available

    def __repr__(self):
        return '<Offer {0}'.format(self.offer_id)


#The applications table is a many-to-many relationship
#https://pythonhosted.org/Flask-SQLAlchemy/models.html
#suggests using an explicit table
#http://docs.sqlalchemy.org/en/rel_0_9/orm/relationships.html#relationships-many-to-many
#http://docs.sqlalchemy.org/en/rel_0_9/core/constraints.html?highlight=constraints
#http://stackoverflow.com/questions/10059345/sqlalchemy-unique-across-multiple-columns
#This table should have a composite primary-key for student_id&position_id
#eliminates need for constraint should 
#However, what if a person recinds an application and then reapplies?
#Do we allow this? if so, we need to add submission time/date stamp