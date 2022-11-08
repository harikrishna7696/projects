import mysql.connector as sql
from datetime import datetime

db = sql.connect(host='localhost',user='root', passwd='Mr@Anonymous76', database='phonebook')
curr = db.cursor()

class Register:
    def __init__(self, email, password, phone, name):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        now = datetime.now()
        self.dt_string = now.strftime("%Y-%m-%d-%H:%M:%S")
        
    def Store(self):
        curr.execute('INSERT INTO customer_details VALUES(%s, %s, %s, %s, %s)', (self.email, self.password, self.phone, self.dt_string, self.name))
        db.commit()
        
        
class Login:
        def __init__(self, email, passwd):
            self.email = email
            self.passwd = passwd
        def log(self):
            curr.execute('SELECT cust_name FROM customer_details WHERE email=%s AND passwd=%s', (self.email, self.passwd))
            for i in curr:
                if i != None:
                    print(i)
                    print('1) Add Contact ')
                    print('2) Read All Contacts ')
                    print('3) Read any specific contact')
                    print('4) Update any specific contact')
                    print('5) Delete any specific contact')  
                    print('6) Delete all contacts')
                    n = int(input("Please Enter Your Option: "))
                    return n
                else:
                    print("Please Check Your Email and Password: ")
                
                
        def ReadAll(self):
            curr.execute('SELECT contact_ID, FirstName, LastName, contact_email, Phone_no FROM phone_book WHERE email=%s', (self.email,))
            for i in curr:
                print(i)
                
        def AddContact(self, FirstName, LastName, contact_email, Phone_no):
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d-%H:%M:%S")
            curr.execute('INSERT INTO phone_book (email, FirstName, LastName, contact_email, Phone_no, created_time)  VALUES(%s, %s, %s, %s, %s, %s)', (self.email, FirstName, LastName, contact_email, Phone_no, dt_string))
            db.commit()
            
        def ReadAnyContact(self, Phone):
            curr.execute('SELECT contact_ID, FirstName, LastName, contact_email, phone_no FROM phone_book WHERE email=%s AND phone_no=%s',  (self.email, Phone))
            for i in curr:
                print(i)
                
        def UpdateAnyContact(self):
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d-%H:%M:%S")
            print("----What do you want to Update---")
            phone_no = input("Enter Phone No to Update Details: ")
            print('1) FirstName: ')
            print('2) LastName: ')
            print('3) contact_email: ')
            print('4) phone_no')
            n = int(input("Select your option: "))
            change_value = input("Enter here: ")
            if n == 1:
                 curr.execute('UPDATE phone_book SET FirstName=%s, created_time=%s  WHERE email=%s AND phone_no=%s', (change_value, dt_string, self.email, phone_no))
            elif n == 2:
                curr.execute('UPDATE phone_book SET LastName=%s, created_time=%s  WHERE email=%s AND phone_no=%s', (change_value, dt_string, self.email, phone_no))
            elif n == 3:
                curr.execute('UPDATE phone_book SET contact_email=%s, created_time=%s  WHERE email=%s AND phone_no=%s', (change_value, dt_string, self.email, phone_no))
            elif n == 4:
                curr.execute('UPDATE phone_book SET phone_no=%s, created_time=%s  WHERE email=%s AND phone_no=%s', (change_value, dt_string, self.email, phone_no))
            db.commit()
            print("changed to: ", change_value)
            
            
        def DeleteAnyContact(self):
            phone_no = input("Enter Phone no to delete: ")
            curr.execute('DELETE FROM phone_book WHERE email=%s AND phone_no=%s', (self.email, phone_no))
            db.commit()
            print("Deleted Contact: ", phone_no)
            
        def DeleteAllContact(self):
            curr.execute('DELETE FROM phone_book WHERE email=%s', (self.email,))
            db.commit()
            print("Deleted All Contacts")