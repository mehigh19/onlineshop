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
                print('Invalid option, input 1, 2 or 3 or 9 to exit')
        except ValueError:
                print('Invalid option, input 1, 2 or 3 or 3 or 9 to exit')

welcome = firstMenu()

def secondMenu():
    check=input('Do you wanna open the menu ? Type yes or no:  ')
    control=Account()
    admin=control.checkAdmin(welcome[1])         #welcome[1] = email

    if check == 'yes' or 'Yes':
        # userExit=False
        while True:
            try:
                if admin == 1:
                    acc=input('---------------'+
                            '\nInput a number:'+
                            '\n1.Product list'+
                            '\n2.Product details'+
                            '\n3.Place an order'+
                            '\n4.Change an order'+
                            '\n5.Change order info'+
                            '\n6.Return'+
                            '\n7.Complaints'+
                            '\n8.Cancel an order'+
                            '\n9.Exit'+
                            '\n10.Add Product'+
                            '\n---------------'+
                            '\n')
                    if int(acc) == 10:
                        print("Ok let's add some products")
                else:
                    acc=input('---------------'+
                            '\nInput a number:'+
                            '\n1.Product list'+
                            '\n2.Product details'+
                            '\n3.Place an order'+
                            '\n4.Change an order'+
                            '\n5.Change order info'+
                            '\n6.Return'+
                            '\n7.Complaints'+
                            '\n8.Cancel an order'+
                            '\n9.Exit'+
                            '\n---------------'+
                            '\n')
                acc = int(acc)
                if acc == 1:
                    print('No products available at te moment')
                elif acc == 2:
                    print('No products available at te moment')
                elif acc == 3:
                    print('Order closed at the moment')
                elif acc == 4:
                    print('Order closed at the moment')
                elif acc == 5:
                    print('Order closed at the moment')
                elif acc == 6:
                    print('Order closed at the moment')
                elif acc == 7:
                    print('No products available at te moment')
                elif acc == 8:
                    print('Order closed at the moment')
                elif acc == 9:
                    return
                else:
                    print('Invalid option')
            except ValueError:
                    print('Invalid option, input one of the numbers that is shown in the menu')

if welcome[0] == True:                           #welcome[0] = loggedIn
    secondMenu()