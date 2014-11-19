from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from internaljobmarket.database import Base



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

class StudentModel(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True)
    studentUid = Column(String(120), unique=True)
    applications = relationship("Applications", backref="studentModel")

    #application = relationship("application", backref='student')

    def __init__(self, student_id=None,
                studentUid=None):
        self.student_id = student_id
        self.studentUid =  studentUid
        self.applications = applications
        

    def __repr__(self):
        return '<Student {0}>'.format(self.studentUid)

class SupervisorModel(Base):
    __tablename__ = 'supervisor'
    supervisor_id = Column(String(50), primary_key=True)
    nameLast = Column(String(120))
    position = relationship("position", backref='supervisor')

    def __init__(self, supervisor_id=None, 
                nameLast=None):
        self.supervisor_id = supervisor_id
        self.nameLast = nameLast
        
    def __repr__(self):
        return '<Supervisor {0}>'.format(self.supervisor_id)

class PositionModel(Base):
    __tablename__ = 'position'
    position_id  = Column(Integer, primary_key=True)
    title = Column(String(120))
    supervisor_id = Column(String(120), ForeignKey("supervisor.supervisor_id"))
    students = relationship("StudentModel", secondary="applications")
    #application = relationship("application", backref='position')

    def __init__(self, position_id=None,
                title=None, supervisor_id=None):
        self.position_id = position_id
        self.title = title
        self.supervisor_id = supervisor_id

    def __repr__(self):
        return '<Position {0}>'.format(self.position_id)


#The applications table is a many-to-many relationship
#https://pythonhosted.org/Flask-SQLAlchemy/models.html
#suggests using an explicit table
#http://docs.sqlalchemy.org/en/rel_0_9/orm/relationships.html#relationships-many-to-many
#This table should have a composite primary-key for student_id&position_id
#eliminates need for constraint should 
#However, what if a person recinds an application and then reapplies?
#Do we allow this? if so, we need to add submission time/date stamp


applications = Table("applications", Base.metadata,
    app_id = Column(Integer, primary_key=True),
    Column(Integer, ForeignKey('position.position_id')),
    Column(Integer, ForeignKey('student.student_id'))
    )


class ApplicationModel(Base):
    'This must be changed to a table, not Model,'
    'because this is an intersection able'
    __tablename__ = 'app_main'
    app_id = Column(Integer, primary_key=True)
    offer = relationship('OfferModel', backref='app_main')

    def __init__(self, app_id=None,
                student_id=None,
                position_id=None):

        self.app_id = app_id
        
        


class OfferModel(Base):
    "This is a one-to-one from Application w/ Y or N"
    #This can rely on the application id completely
    __tablename__ = 'offer'
    offer_id = Column(Integer, primary_key=True)
    app_id = Column(Integer, ForeignKey('application'))
    offerMade = Column(String(120))
    offer_date = Column(String(120))
    response = Column(String(120))
    response_date = Column(String(120))
    available = Column(String(120))

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

'''