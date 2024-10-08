import mysql.connector

class Account():
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='db',
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.con.cursor()

    def signUp(self,firstname,lastname,email,password):
        query = 'INSERT INTO `onlineshop` (`firstName`, `lastName`, `email`, `password`,`admin`) VALUES(%s,%s,%s,%s,%s)'
        values = (firstname,lastname,email,password,0)
        self.cursor.execute(query, values)
        self.con.commit()
        self.cursor.close()
        self.con.close()
        return 'Succesfully logged in'

    def signIn(self):
        email=input('Please input your email:  ')
        password=input('Please input your password:  ')
        query = 'SELECT email, password FROM onlineshop WHERE email = %s AND password = %s'
        self.cursor.execute(query, (email, password))
        result = self.cursor.fetchone()
        self.cursor.close()
        self.con.close()
        return result,email
    
    def checkAdmin(self,email):
        query = 'SELECT admin, email FROM onlineshop WHERE admin = %s AND password = %s'
        try:
            self.cursor.execute(query, (1, email))
            result = self.cursor.fetchone()
            self.cursor.close()
            self.con.close()
            return result[0]
        except Exception:
            pass