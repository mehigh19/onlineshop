from Account import Account
import re

def welcome():
    acc=input('Welcome to 3Market.com'+
            '\nInput a number:'+
            '\n1.Sign up'+
            '\n2.Sign in'+
            '\n3.Product list'+
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
            account=Account(firstname,lastname,email,password)
            account.signIn()
        elif acc == 2:
            print('Enter account details')
        elif acc ==3:
            print('No products available at te moment')
        else:
            print('Invalid option, imput 1, 2 or 3')
    except ValueError:
            print('Invalid option, imput 1, 2 or 3')

welcome()