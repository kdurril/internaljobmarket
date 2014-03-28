#Populate the database

import sqlite3

conn = sqlite3.connect("Ga_app_db.db")
curs = conn.cursor()


#Add student records
with open("student_dev.csv", "r+") as infile:
    dr = csv.DictReader(infile, delimiter = ',')

to_db = [(i['studentUid'], i['nameLast'], i['nameFirst'], i['email'],\
        i['phone'], i['major'], i['programCode'], i['semBegin'],\
        i['student_id'], i['graduationExpected'], i['creditFall'],\
        i['creditSpring'], i['request201408'], i['request201501']) for i in dr]

curs.executemany('''INSERT INTO student (
    studentUid, nameLast, nameFirst, email, 
    phone, major, programCode, semBegin, 
    student_id, graduationExpected, creditFall, 
    creditSpring, request201408, request201501) 
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', to_db)
conn.commit()

#Add supervisor records
with open("supervisor_dev.csv", "r+") as infile:
    dr = csv.DictReader(infile, delimiter = ',')

to_do = [(i['nameLast'], i['nameFirst'], i['phone'], i['email'], i['room'],\
        i['center'],  i['supervisor_id']) for i in dr]

curs.executemany('''INSERT INTO supervisor (
    nameLast, nameFirst, phone, email, room, center, supervisor_id)
    VALUES (?,?,?,?,?,?,?);''', to_db)
conn.commit()
