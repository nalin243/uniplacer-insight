import bcrypt
import random
import smtplib
from email.message import EmailMessage

from mysql.connector import connect

import json
import os

class LoginAuth():
    
    def __init__(self, appstorage):
        self.appstorage = appstorage
        self.userid, self.password, self.Host, self.dbName = self.appstorage.getDbCredentials()

        self.smtpEmail = None
        self.smtpPass = None

        dirpath = os.path.dirname(__file__)+"/../mailconfig.json"

        with open(dirpath) as mailconfig:
            parsedMailConfig = json.loads(mailconfig.read())

            self.smtpEmail = "{}".format(parsedMailConfig["SMTP_EMAIL"])
            self.smtpPass = "{}".format(parsedMailConfig["SMTP_PASS"])

        self.connection  = None
        self.cursor = None

        try:
            self.connection = connect(host=self.Host, user=self.userid, password =self.password, database = self.dbName)
            self.cursor = self.connection.cursor()
            self.cursor.execute("create table if not exists users ( username varchar(20), email varchar(100), password varchar(100) )")
        except Exception as e:
            pass

        self.username = None
        self.otp = None

    def establishConn(self):   
        self.userid, self.password, self.Host, self.dbName = self.appstorage.getDbCredentials() 
        try:
            self.connection = connect(host=self.Host, user=self.userid, password =self.password, database = self.dbName)
            self.cursor = self.connection.cursor()
            self.cursor.execute("create table if not exists users ( username varchar(20), email varchar(100), password varchar(100) )")
        except Exception as e:
           pass

    def setUsername(self,username):
        self.username = username

    
    # Login Authentication Module
    def checkAuth(self, username, password):

        self.query = "select * from users where username = '{}'".format(username) 
        self.cursor.execute(self.query)

        try:
            _,self.mail,hashedpass = self.cursor.fetchall()[0]

            if bcrypt.checkpw(password.encode('utf-8'), hashedpass.encode('utf-8')):
                return True
            else:
                return False

        except Exception as e:
            return False

    # OTP Authentication Module
    def sendOtp(self):
        self.query = "select * from users where username = '{}'".format(self.username) 
        self.cursor.execute(self.query)

        _,mail,_ = self.cursor.fetchall()[0]

        self.otp = random.randint(10000, 99999)

        msg = EmailMessage()
        msg.set_content("Your OTP is: {}".format(str(self.otp)))
        msg['Subject'] = 'Password Change Request'
        msg['From'] = "Uni-Placer Insight"
        msg['To'] = "{}".format(mail)

        self.s = smtplib.SMTP('smtp.gmail.com', 587)
        self.s.starttls()
        self.s.login(self.smtpEmail, self.smtpPass)
        self.s.send_message(msg)
        self.s.quit()

    def checkOtp(self, otp):
        if str(self.otp) == str(otp):
            return True
        else:
            return False
        
    # Updating user credentials module    
    def newCredentials(self, newMail, confirmPass):

        hashedPass = bcrypt.hashpw(confirmPass.encode('utf-8') ,bcrypt.gensalt())

        updateNewCreds = "update users set email = '{}', password = '{}' ".format(newMail, str(hashedPass.decode("utf-8")))
        self.cursor.execute(updateNewCreds)
        self.connection.commit()
        return True


