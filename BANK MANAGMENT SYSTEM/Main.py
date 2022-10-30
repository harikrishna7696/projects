from mainOptions import CreateAccount, Login
print('*------------*-------------*----->WELCOME TO HKBANK<------*-----------*-------------*')
print()
print('1) Create Account(New Customer)')
print('2) Login (Existing Customer)')
print('3) Exit')
n = int(input('Please Enter Your Option: '))
if n == 1:
    CreateAccount()
elif n == 2:
    Login()