#Models
#keep basic sql for testing purposes

qry_student = ''' SELECT student_id,
                studentUid,
                nameLast,
                nameFirst,
                email,
                phone,
                major,
                programCode,
                semBegin,
                graduationExpected,
                creditFall,
                creditSpring,
                request201408,
                request201501 
                FROM student  
                '''

qry_supervisor = ''' SELECT supervisor_id,
                    nameLast,
                    nameFirst,
                    phone,
                    email,
                    room,
                    center
                    FROM supervisor_id 
                    '''

qry_position = ''' SELECT position_id,
                    title,
                    workGroup,
                    position_type,
                    course,
                    programMin,
                    programStd,
                    positionOverview,
                    primaryDuties,
                    necessarySkill,
                    preferredSkill,
                    dateOpen,
                    dateClosed,
                    available,
                    supervisor_id
                    FROM position 
                    '''

qry_application = ''' SELECT app_id,
                      student_id,
                      position_id
                      FROM application 
                      '''

qry_offer = ''' SELECT offer_id,
                app_id,
                offerMade, 
                offer_date, 
                response,
                response_date,
                available
                FROM offer
                '''