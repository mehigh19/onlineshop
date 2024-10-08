from Account import Account
import re

def firstMenu():
    loggedIn=False
    print('Welcome to 3Market.com')
    while loggedIn == False:
        acc=input('---------------'+
                '\nInput a number:'+
                '\n1.Sign up'+
                '\n2.Sign in'+
                '\n3.Product list'+
                '\n9.Exit'
                '\n---------------'+
                '\n')
        try:
            acc=int(acc)
            if acc == 1:
                firstname=input('Input your first name: ')
                lastname=input('Input your last name: ')
                if firstname =='' or lastname =='':
                    print('Error, you need to input your name correctly')
                    return
                email=input('Input your email: ')
                valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
                if not valid:
                    print('Your mail is invalid')
                    return
                password=input('Input your password, your password needs to have atleast 5 characters and a number: ')
                if len(password) <5 or not any(char.isdigit() for char in password):
                    print('Your password needs to have atleast 5 characters and a number')
                    return
                account=Account()
                print(account.signUp(firstname,lastname,email,password))
            elif acc ==9:
                break
            elif acc == 2:
                account2=Account()
                result,email=account2.signIn()
                if result:
                    print('Loggin successful! You are connected')
                    loggedIn=True
                    return loggedIn, email
                else:
                    print('Loggin failed ! Email or password not found')
            elif acc ==3:
                print('No products available at te moment')
            else:
                print('Invalid option, input 1, 2 or 3')
                break
        except ValueError:
                print('Invalid option, input 1, 2 or 3')

welcome = firstMenu()

if isinstance(welcome, tuple):
    if welcome[0] == True:                           #welcome[0] = loggedIn
        control=Account()
        admin=control.checkAdmin(welcome[1])         #welcome[1] = email
        if admin == 1:
            print(f'Welcome back admin')