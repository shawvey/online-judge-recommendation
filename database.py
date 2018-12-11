import sqlite3

class Db:
    def __init__(self):
                self.connection = sqlite3.connect("database/login.db")
                self.createTable()

    def createTable(self):
                #connection = sqlite3.connect("login.db")
        
        self.connection.execute("CREATE TABLE IF NOT EXISTS STUDENTS(USERNAME TEXT NOT NULL, PASSWORD TEXT)")        
        self.connection.commit()

    def insertTable(self,user,password):
        print(user)
        print(password)
        self.connection.execute("INSERT INTO STUDENTS VALUES(?,?)",(user,password))
        self.connection.commit()

                
    def loginCheck(self,username,password):
        result = self.connection.execute("SELECT * FROM STUDENTS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        count = len(result.fetchall())
        print(count)
        #print(result.fetchall())
        for data in result:
            print("Username : ", data[1])
            print("Password : ", data[2])
        if(count > 0):
            print("Login Successfully")
            return True
                
        else:
            print("You havent registered yet")
            return False


        
