from functions import Register, Login


print('1. Registration')
print('2. Login (If user is already registered)')


n = int(input("Enter Your Option: "))

# if user enter 1 it takes require arguments from user and create account by given input
# it also store time when the account is created
if n == 1:
    name = input('Name: ')
    email = input('Email: ')
    phone = input('Phone No: ')
    password = input('Password: ')
    user = Register(email, password, phone, name)
    user.Store()
 
# if user enter 2 it asked for email and password 
# give access to see or modify the contacts   
elif n == 2:
    email = input('Email: ')
    password = input('Password: ')
    user = Login(email, password)
    o =user.log()
    
    if o == 1:
        first = input('Enter contact first name: ')
        last = input('Enter contact last name: ')
        phone = input('Enter contact phone number: ')
        email = input('Enter contact email: ')
        user.AddContact(first, last, email, phone)
    elif o == 2:
        user.ReadAll()
    elif o == 3:
        phone_no = input("enter phone number to see details: ")
        user.ReadAnyContact(phone_no)
    elif o == 4:
        user.UpdateAnyContact()
    elif o == 5:
        user.DeleteAnyContact()
    elif o == 6:
        user.DeleteAllContact()
    else:
        print("Please Provide Valid Details:  ")
else:
    print("Enter Valid Option: ")