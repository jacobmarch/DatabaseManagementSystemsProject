#Import sqlite3
import sqlite3 as sql

#Connect to database
conn = sql.connect('database.db')

#Create a cursor
cursor = conn.cursor()

#Create Employee table
cursor.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEE (
    SSN INTEGER PRIMARY KEY NOT NULL,
    Fname TEXT,
    Lname TEXT,
    Minit TEXT,
    Salary INTEGER,
    Birthday DATE,
    Address TEXT,
    JobTitle TEXT,
    CHECK (JobTitle = 'Doctor'),
    CHECK (JobTitle = 'Nurse'),
    CHECK (JobTitle = 'Technician')
)""")
               

#Create Patient table
cursor.execute("""CREATE TABLE IF NOT EXISTS PATIENT (
    ID INTEGER PRIMARY KEY NOT NULL,
    Fname TEXT,
    Lname TEXT,
    Minit TEXT,
    Insurance TEXT,
    TotalCost INTEGER,
    Address TEXT
)""")

#Create Visitor table
cursor.execute("""CREATE TABLE IF NOT EXISTS VISITOR (
    PatientID INTEGER NOT NULL,
    Phone TEXT NOT NULL,
    Fname TEXT,
    Lname TEXT,
    Minit TEXT,
    PRIMARY KEY (PatientID, Phone)
)""")

#Create EmployeePhone table
cursor.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEE_PHONE (
    SSN INTEGER PRIMARY KEY NOT NULL,
    Phone TEXT
)""")

#Create PatientPhone table
cursor.execute("""CREATE TABLE IF NOT EXISTS PATIENT_PHONE (
    PatientID INTEGER PRIMARY KEY NOT NULL,
    Phone TEXT
)""")

#Create PatientDiagnosis table
cursor.execute("""CREATE TABLE IF NOT EXISTS PATIENT_DIAGNOSIS (
    PatientID INTEGER PRIMARY KEY NOT NULL,
    Diagnosis TEXT
)""")

#Create Department table
cursor.execute("""CREATE TABLE IF NOT EXISTS DEPARTMENT (
    Dnumber INTEGER PRIMARY KEY NOT NULL,
    NumberOfEmployees INTEGER,
    Dlocation TEXT,
    Dname TEXT
)""")

#Create Machines table
cursor.execute("""CREATE TABLE IF NOT EXISTS MACHINES (
    ModelNumber INTEGER PRIMARY KEY NOT NULL,
    Type TEXT,
    Dnumber INTEGER,
    FOREIGN KEY (Dnumber) REFERENCES DEPARTMENT (Dnumber)
)""")

#Create Medications table
cursor.execute("""CREATE TABLE IF NOT EXISTS MEDICATIONS (
    Name TEXT PRIMARY KEY NOT NULL,
    DiseasesTreated TEXT,
    Cost INTEGER,
    SideEffects TEXT
)""")

#Create Rooms table
cursor.execute("""CREATE TABLE IF NOT EXISTS ROOMS (
    RoomNumber INTEGER PRIMARY KEY NOT NULL,
    Dnumber INTEGER
)""")

#Create WorksIn table
cursor.execute("""CREATE TABLE IF NOT EXISTS WORKS_IN (
    SSN INTEGER NOT NULL,
    Dnumber INTEGER NOT NULL,
    Hours INTEGER,
    PRIMARY KEY (SSN, Dnumber)
)""")

#Create Uses table
cursor.execute("""CREATE TABLE IF NOT EXISTS USES (
    SSN INTEGER NOT NULL,
    ModelNumber INTEGER NOT NULL,
    DateUsed DATE,
    PRIMARY KEY (SSN, ModelNumber)
)""")

#Create UsedToTreat table
cursor.execute("""CREATE TABLE IF NOT EXISTS USED_TO_TREAT (
    MedicationName TEXT PRIMARY KEY NOT NULL,
    Diagnosis TEXT NOT NULL
)""")
               
#Create Appointment table
cursor.execute("""CREATE TABLE IF NOT EXISTS APPOINTMENT (
    AppointmentNumber INTEGER PRIMARY KEY NOT NULL,
    PatientID INTEGER,
    NurseSSN INTEGER,
    DoctorSSN INTEGER,
    AppointmentDate DATE,
    AppointmentTime TIME,
    FOREIGN KEY (PatientID) REFERENCES PATIENT(PatientID),
    FOREIGN KEY (NurseSSN) REFERENCES EMPLOYEE(SSN),
    FOREIGN KEY (DoctorSSN) REFERENCES EMPLOYEE(SSN)
)""")

#Commit changes
conn.commit()