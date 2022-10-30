import mysql.connector as sql
from datetime import datetime
db = sql.connect(host='localhost', user='root',passwd='Mr@Anonymous76', database='hkbank')
cur = db.cursor()


# Creating account with given data
def CreateAccount():
    try:
        # taking input from the user to create account
        print('Creating Your Account.......')
        account_no = int(input('Enter Numbers 11: '))
        if len(str(account_no)) != 11:
            print("Please Enter 11 Numbers: ")
            account_no = int(input("Enter 11 Numbers: "))
        cust_name = input('Enter Your Name: ')
        password = input('Enter New Password: ')
        cust_phone = int(input("Please Enter 10 Numbers: "))
        if len(str(cust_phone)) != 11:
            print("Please Enter 11 Numbers: ")
            cust_phone = int(input("Please Enter 10 Numbers: "))
        amount_dp = float(input("Please Enter Deposit amount: "))
        today = datetime.now()
        d1 = today.strftime("%Y-%m-%d-%H:%M:%S")
        
        # sql query that insert values into databases
        sql_query = "INSERT INTO customer_details VALUES(%s, %s, %s, %s, %s, %s)"
        val = (account_no, cust_name, password,cust_phone, amount_dp, d1)
        cur.execute(sql_query, val)
        print("Your Account Has been Created: ")
        db.commit()
    except Exception:
        print('Something Went Wrong Try Again Later...')


def menu():
    print('1) Withdraw Amount')
    print('2) Transactions')
    print('3) Customer Details')
    print('4) Update Password')
    print('5) Delete Account')
    print('6) Quit')
     
     
def extract(c):
        for i in c:
            return i     

# login function it logins using the username and password
def Login():
    try:
        username = input('Please Enter Username: ')
        password = input('Please Enter Your Password: ')
        cur.execute("SELECT account_no, cust_name, cust_phone, amount_dp,passwd FROM customer_details WHERE cust_name = %s and passwd= %s", (username, password))
        # extracting all values for further  function
        details = extract(cur) # extracting from user
        # account number
        account_no = details[0]
        # customer name
        cust_name = details[1]
        # customer phone
        cust_phone = details[2]
        # Balance Amount
        amount_bal = details[3]
        passwd = details[4]
        # After Login Successfull
        print('Account: ', account_no)
        print('Amount: ', amount_bal)
        print('Login Success. Happy Banking!')
        # printing menu
        menu()  
    except Exception:
        print('Something Went Wrong Try Again Later...')
        
        
    # Option 5) Delete User Function
    def DeleteAccount():
        try:
            # using account deleting the user from customer table using account no
            cur.execute('DELETE FROM transactions WHERE account_no=%s', (account_no, ))
            db.commit()
            # also deleting the transaction using account no
            cur.execute('DELETE FROM customer_details WHERE account_no=%s', (account_no,))
            db.commit()
            # After deleting
            print('Deleted Your Account: ', cust_name)
            print('Hope you come back soon.....')
        except Exception:
            print('Something Went Wrong Try Again Later...')    
            
            
    # Option 4) Update Password
    def UpdatePassword():
        try:
            # Printing current password
            print('Your Password: ', passwd)
            # new password input
            new_pass = input('Enter: ')
            # updating the password using
            cur.execute('UPDATE customer_details set passwd=%s WHERE account_no=%s', (new_pass, account_no))
            # after updating password
            print('Password Changed To: ', new_pass)
            db.commit()
        except Exception:
            print('Something Went Wrong Try Again Later...')
      
    # Option 3) Custer Details function
    def CustomerDetails():
        try:
            # printing the data of user
            print('Name: ', cust_name)
            print('Phone No: ', cust_phone)
            print('Account No: ', account_no)
            # checking user want to see password
            p = int(input("Enter 1 To see password: "))
            # if user enters 1 password will shown else not
            if p == 1:
                print('Password: ', password)
        except Exception:
            print('Something Went Wrong Try Again Later...')
            
    # Option 2) Transaction
    def Transactions():
        try:
            # extracting transactiong using account no 
            cur.execute('SELECT * from transactions WHERE account_no=%s',(account_no, ))
            # printing the transactions
            for i in cur:
                print('Account ', 'Withdrawn','Balance Amt', 'Transaction Time')
                print(i)
        except Exception:
            print('Something Went Wrong Try Again Later...')
            
    # Option 1) Withdraw Function        
    def Withdraw():
        try:
            # Taking amount to Withdraw
            withdraw = int(input('Please Enter Amount: '))
            # balance amount after withdrawn
            bal_amt = amount_bal - withdraw
            if amount_bal <= 0:
                # if amount less than or equal to zero print this message and return 
                print("Your Balance is: 0")
                return
            elif withdraw <= 0:
                # if user enter amount less than or equal to zero print this message and return 
                print("Please Enter Greater Than 0: ")
                return
            elif withdraw > amount_bal:
                # if withdraw amount greater than bal amount print this message and return 
                print("Insufficient Funds: ")
                return
            else:
                # current time and data
                today = datetime.now()
                d1 = today.strftime("%Y-%m-%d-%H:%M:%S")
                # entering values into transaction table with time
                cur.execute('UPDATE customer_details SET amount_dp=%s WHERE cust_name=%s AND passwd=%s', (bal_amt,username, password))
                cur.execute('INSERT INTO transactions values(%s, %s, %s, %s)', (account_no, withdraw, bal_amt, d1))
                db.commit()
                print('Your Current_bal: ', bal_amt)
            print("Thank You For Banking With Us....")
            return
        except Exception:
            print('Something Went Wrong Try Again Later...')
        
        
    n = int(input("Choose Option: ")) 
    if n >= 1 and n <= 5:  
        if n == 1:
            Withdraw()
        elif n == 2:
            Transactions()
        elif n == 3:
            CustomerDetails()
        elif n == 4:
            UpdatePassword()
        elif n == 5:
            DeleteAccount()
    else:
        print('Please Choose Correct One: ')
            