from sqlalchemy import Column, Integer, String
from internaljobmarket.database import Base

class StudentModel(Base):
    __tablename__ = 'student'
    student_id = Column(String(50), primary_key=True)
    studentUid = Column(String(120))
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
        self.nameLast, = nameLast
        self.nameFirst = nameFirst
        self.email = email
        self.phone = phone
        self.major = major
        self.programCode = programCode
        self.semBegin = semBegin
        self.graduationExpected = graduationExpected
        self.creditFall = creditFall
        self.creditSpring = CreditSpring
        self.request201408 = request201408
        self.request201501 = request201501

class SupervisorModel(Base):
    __tablename__ = 'supervisor'
    supervisor_id = Column(String(50), primary_key=True)
    nameLast = Column(String(120))
    nameFirst = Column(String(120))
    phone = Column(String(120))
    email = Column(String(120))
    room = Column(String(120))
    center = Column(String(120))

    def __init__(self, supervisor_id=None, 
                nameLast=None, nameFirst=None,
                phone=None, email=None,
                room=None, center=None):
        self.supervisor_id = supervisor_id
        self.nameLast = nameLast
        self.nameFirst = nameFirst
        self.phone = phone
        self.email = email
        self.room = room
        self.center = center

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
    supervisor_id = Column(String(120))

    def __init__(self, position_id=None,
                title=None, workGroup=None, position_type=None,
                course=None, programMin=None, programStd=None,
                positionOverview=None, primaryDuties=None,
                necessarySkill=None, preferredSkill=None,
                dateOpen=None, dateClosed=None,
                available=None, supervisor_id=None):
        self.selfposition_id = position_id
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

class ApplicationModel(Base):
    __tablename__ = 'application'
    app_id = Column(Integer, primary_key=True)
    student_id = Column(String(120))
    position_id = Column(Integer, primary_key=True)

    def __init__(self, app_id=None,
                student_id=None,
                position_id=None):

        self.app_id = app_id
        self.student_id = student_id
        self.position_id = position_id

class OfferModel(Base):
    __tablename__ = 'offer'
    offer_id 
    app_id
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