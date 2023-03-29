#Import sqlite3
import sqlite3 as sql

#Connect to database
conn = sql.connect('databaseHayden.db')

#Create a cursor
cursor = conn.cursor()

#Create a query and execute it
cursor.execute("""SELECT Fname, Lname
                  FROM EMPLOYEE
                  WHERE JobTitle = 'doctor';""")

cursor.execute("""SELECT M.ModelNumber, D.Dlocation
                  FROM MACHINES M
                  JOIN DEPARTMENT D ON M.Dnumber = D.Dnumber;""")

cursor.execute("""SELECT P.ID, P.Fname AS PatientFirstName, P.Lname AS PatientLastName, E.Fname AS NurseFirstName, E.Lname AS NurseLastName
                  FROM PATIENT P
                  JOIN APPOINTMENT A ON P.ID = A.PatientID
                  JOIN EMPLOYEE E ON A.NurseSSN = E.SSN;""")

cursor.execute("""SELECT V.Fname, V.Lname, V.Phone
                  FROM VISITOR V
                  WHERE V.PatientID = 2;""")

cursor.execute("""SELECT Fname, Lname
                  FROM EMPLOYEE
                  WHERE Salary > 75000;""")

cursor.execute("""SELECT A.PatientID, P.Fname AS PatientFirstName, P.Lname AS PatientLastName, EN.Fname AS NurseFirstName, EN.Lname AS NurseLastName, ED.Fname AS DoctorFirstName, ED.Lname AS DoctorLastName
                  FROM APPOINTMENT A
                  JOIN PATIENT P ON A.PatientID = P.ID
                  JOIN EMPLOYEE EN ON A.NurseSSN = EN.SSN
                  JOIN EMPLOYEE ED ON A.DoctorSSN = ED.SSN
                  WHERE A.AppointmentDate = DATE('now');""")

cursor.execute("""SELECT AVG(Salary) AS AvgSalary
                  FROM EMPLOYEE
                  WHERE SSN IN (SELECT SSN FROM WORKS_IN WHERE Dnumber = 2);""")

cursor.execute("""SELECT P.ID, P.Fname, P.Lname
                  FROM PATIENT P
                  JOIN PATIENT_DIAGNOSIS PD ON P.ID = PD.PatientID
                  GROUP BY P.ID, P.Fname, P.Lname
                  HAVING COUNT(PD.Diagnosis) > 1;""")

cursor.execute("""SELECT A.AppointmentNumber, P.Fname AS PatientFirstName, P.Lname AS PatientLastName, A.AppointmentDate, A.AppointmentTime
                  FROM APPOINTMENT A
                  JOIN PATIENT P ON A.PatientID = P.ID
                  JOIN EMPLOYEE E ON A.DoctorSSN = E.SSN
                  WHERE E.Lname = 'Smith';""")

cursor.execute("""SELECT P.ID, P.Fname, P.Lname
                  FROM PATIENT P
                  JOIN ROOMS R ON P.ID = R.PatientID
                  WHERE R.RoomType = 'standard';""")

#Commit changes
conn.commit()