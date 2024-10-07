import mysql.connector

class Account():
    def __init__(self,firstname,lastname,email,password):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.password=password
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='db',
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.con.cursor()
    def signIn(self):
        query = 'INSERT INTO `onlineshop` (`firstName`, `lastName`, `email`, `password`) VALUES(%s,%s,%s,%s)'
        values = (self.firstname,self.lastname,self.email,self.password)
        self.cursor.execute(query, values)
        self.con.commit()
        self.cursor.close()
        self.con.close()
        print(query, values)