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
            print('Create account')
        elif acc == 2:
            print('Enter account details')
        elif acc ==3:
            print('No products available at te moment')
        else:
            print('Invalid option, imput 1, 2 or 3')
    except ValueError:
            print('Invalid option, imput 1, 2 or 3')

welcome()