#GA PROCESS
#DB Create

import sqlite3

#sqlite3 db from student records

conn = sqlite3.connect("Ga_app_db.db")
curs = conn.cursor()

'''
clear_table = ['DROP TABLE if exists supervisor;',\
'DROP TABLE if exists student;',\
'DROP TABLE if exists position;',\
'DROP TABLE if exists positionApp;',\
'Drop TABLE if exists offer']

for table in clear_table:
    curs.execute(table)
    conn.commit()
'''

qry_student_table = '''CREATE TABLE student (
student_id TEXT PRIMARY KEY,
studentUid INTEGER,
nameLast TEXT NOT NULL,
nameFirst TEXT NOT NULL,
email TEXT NOT NULL,
phone TEXT,
major TEXT,
programCode TEXT,
semBegin TEXT,
graduationExpected TEXT,
creditFall TEXT,
creditSpring TEXT,
request201408 TEXT,
request201501 TEXT
);'''
curs.execute(qry_student_table)
conn.commit()

qry_supervisor_table = '''CREATE TABLE supervisor(
supervisor_id TEXT PRIMARY KEY,
nameLast TEXT NOT NULL,
nameFirst TEXT NOT NULL,
phone TEXT,
email TEXT NOT NULL,
room TEXT,
center TEXT
);'''
curs.execute(qry_supervisor_table)
conn.commit()

qry_position_table = '''CREATE TABLE position (
position_id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
workGroup TEXT,
position_type TEXT NOT NULL,
course TEXT,
programMin TEXT,
programStd TEXT,
positionOverview TEXT NOT NULL,
primaryDuties TEXT NOT NULL,
necessarySkill TEXT,
preferredSkill TEXT,
dateOpen Date,
dateClosed Date,
available INTEGER NOT NULL CHECK (available >= 0),
supervisor_id TEXT,
CONSTRAINT FKsupervisor FOREIGN KEY (supervisor_id) REFERENCES supervisor
);'''
curs.execute(qry_position_table)
conn.commit()

qry_positionApp_table = '''CREATE TABLE positionApp (
app_id INTEGER PRIMARY KEY AUTOINCREMENT,
position_id INTEGER, 
student_id TEXT,
CONSTRAINT FKpostion FOREIGN KEY (position_id) REFERENCES position,
CONSTRAINT FKstudent FOREIGN KEY (student_id) REFERENCES student,
CONSTRAINT CHK_student_position UNIQUE (position_id, student_id)
); '''
curs.execute(qry_positionApp_table)
conn.commit()

qry_offer_table = '''CREATE TABLE offer (
offer_id INTEGER PRIMARY KEY AUTOINCREMENT ,
app_id INTEGER,
offerMade Text, 
offer_date DATE, 
response TEXT,
response_date DATE,
available TEXT,
CONSTRAINT FKpositionApp FOREIGN KEY (app_id) REFERENCES positionApp
);'''
curs.execute(qry_offer_table)
conn.commit()