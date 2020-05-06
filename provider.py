import pymysql
from baseObject import baseObject

class providerList(baseObject):

    def __init__(self):
        self.setupObject('Provider')

    def verifyNew(self,n=0):
        self.errorList = []

        if len(self.data[n]['PCPID']) != 4:
            self.errorList.append("Please Enter a Valid License Number.")

        if len(self.data[n]['DOH']) == 0:
            self.errorList.append("Please input date of hire.")

        if len(self.data[n]['Name']) == 0:
            self.errorList.append("Name cannot be blank.")

        if len(self.data[n]['SSN']) != 9:
            self.errorList.append("Please enter your 9 digit Social Security Number.")

        if len(self.errorList) > 0:
            return False
        else:
            return True
