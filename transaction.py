import pymysql
from baseObject import baseObject

class TransactionList(baseObject):

    def __init__(self):
        self.setupObject('Transaction')

    def verifyNew(self,n=0):
        self.errorList = []

        if len(self.data[n]['TransactionID']) == 0:
            self.errorList.append("Transaction ID cannot be blank.")

        if len(self.data[n]['Date']) == 0:
            self.errorList.append("Please input date of transaction.")

        if len(self.data[n]['Amount cannot be blank']) == 0:
            self.errorList.append("Amount cannot be blank.")

        if len(self.data[n]['Status']) == 0:
            self.errorList.append("Please choose a Status.")

        if len(self.data[n]['PatientID']) == 0:
            self.errorList.append("Please choose which patient account to charge/credit.")

        if len(self.data[n]['PCPID']) == 0:
            self.errorList.append("Please indicate which Provider serviced the patient.")

        if len(self.errorList) > 0:
            return False
        else:
            return True
