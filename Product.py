import mysql.connector

class Product():
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='db',
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.con.cursor()

    def productList(self):
        query = 'SELECT productName, productPrice FROM products'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print('Product name   Price')
        for element in result:
            print(element)
        self.cursor.close()
        self.con.close()

    def productDetails(self):
        productId=input('Input the product id so i can show you the product details')
        query = 'SELECT productName FROM products WHERE id = %s'
        self.cursor.execute(query, (productId,))
        result = self.cursor.fetchone()
        self.cursor.close()
        self.con.close()
        return result[0]

    def productOrder(self):
        return 'Order closed at the moment'

    def orderInfo(self):
        return 'If you wanna change the phone number, the adress or anything else, email us at 3market_order@gmail.com or give us a call at +40754592041'
    
    def returnProduct(self):
        return 'If you wanna return a product email us at 3market_returns@gmail.com or give us a call at +40754592041'
    
    def complaints(self):
        return 'If you have a complaint email us at 3market_complaints@gmail.com and an operator will assist your problem or give us a call at +40754592041'
    
    def cancelOrder(self):
        cancelOrder=('If you want to cancel your order you need to complete the form, after that it can be sent to us at 3market_order@gmail.com or give us a call at +40754592041'+
                    '\nOrder Id: '+
                    '\nOrder Email: '
                    '\nReason: '+
                    '\nRefound Option: card/voucher')
        return cancelOrder
    
    def addProduct(self):
        productName=input('Input product name:  ')
        productPrice=float(input('Input product price:  '))
        productStock=int(input('Input product stock:  '))
        query = 'INSERT INTO `products` (`productName`, `productPrice`, `productStock`) VALUES(%s,%s,%s)'
        values = (productName,productPrice,productStock)
        self.cursor.execute(query, values)
        self.con.commit()
        self.cursor.close()
        self.con.close()
        return f'Succesfully added te product {productName}'