import pymysql
from baseObject import baseObject

class adminList(baseObject):

    def __init__(self):
        self.setupObject('Admin')

    def tryLogin(self,email,pw):
        #SELECT * FROM `Admin` WHERE `username` = 'admin1' AND `password` = '123'
        sql = 'SELECT * FROM `' + self.tn + '` WHERE `username` = %s AND `password` = %s;'
        tokens = (email,pw)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        n=0
        for row in cur:
            self.data.append(row)
            n+=1
        if n > 0:
            return True
        else:
            return False
