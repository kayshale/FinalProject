import pymysql
from baseObject import baseObject

class patientList(baseObject):

    def __init__(self):
        self.setupObject('Patient')

    def verifyNew(self,n=0):
        self.errorList = []

        if len(self.data[n]['PatientID']) == 0:
            self.errorList.append("Patient ID cannot be blank.")

        if len(self.data[n]['DOB']) == 0:
            self.errorList.append("Please input date of birth.")

        if len(self.data[n]['fname']) == 0:
            self.errorList.append("First Name cannot be blank.")

        if len(self.data[n]['lname']) == 0:
            self.errorList.append("Last Name cannot be blank.")

        if len(self.data[n]['SSN']) != 9:
            self.errorList.append("Please enter your 9 digit Social Security Number.")

        if len(self.data[n]['PCPID']) != 4:
            self.errorList.append("Please enter a valid Provider ID.")

        if len(self.errorList) > 0:
            return False
        else:
            return True
