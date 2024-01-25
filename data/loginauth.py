import bcrypt

from mysql.connector import connect

class LoginAuth():
    
    def __init__(self, appstorage):
        self.userid, self.password, self.Host, self.dbName = appstorage.getDbCredentials()

        self.connection = connect(host=self.Host, user=self.userid, password =self.password, database = self.dbName)
        self.cursor = self.connection.cursor()
        self.cursor.execute("create table if not exists users ( username varchar(20), email varchar(100), password varchar(100) )")

        

    def checkAuth(self, username, password):

        self.query = "select * from users where username = '{}'".format(username,password) 
        self.cursor.execute(self.query)
        

        try:
            _,_,hashedpass = self.cursor.fetchall()[0]

            if bcrypt.checkpw(password.encode('utf-8'), hashedpass.encode('utf-8')):
                return True
            else:
                return False

        except Exception as e:
            return False

        