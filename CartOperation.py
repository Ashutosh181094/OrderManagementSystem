import sys
import createDatabaseConnection
import psycopg2
import MainMenu
import random


class Cart:

    def addToCart(self):

        cur = createDatabaseConnection.getDatabaseConnection().createConnection()

        try:
            cur.execute("create table if not exists Cart(productId varchar)")
        except psycopg2.Error as e:
            print("Could Not create table Cart")
            print(e)
            sys.exit(1)

        try:
            print("Please provide the Id of product for Adding to cart")
            productId = input()
            cart_insert_query = """INSERT INTO Cart(productId) VALUES (%s) """
            insertRecord = (productId)
            cur.execute(cart_insert_query, insertRecord)
            print("Product Successfully Added to the Cart")
        except psycopg2.Error as e:
            print("Error Occured while inserting value in database")
            print(e)
            sys.exit(1)
        print("Select Next Operation")
        print("1-Display Cart")
        print("2-Move to Main Menu")
        choice = input()
        if choice == '1':
            self.displayCart()
        elif choice == '2':
            MainMenu.mainMenu().mainMenuOptions()
        else:
            print("Incorrect Option Entered Moving you to Main Menu")
            MainMenu.mainMenu().mainMenuOptions()

    def deleteFromCart(self):
        print("Please provide the product Id that you want to remove from cart")
        product_id = input()

        cur = createDatabaseConnection.getDatabaseConnection().createConnection()

        try:
            sql_delete_query = """Delete from cart where productid = %s"""
            cur.execute(sql_delete_query, product_id)

        except psycopg2.Error as e:
            print("Could Not execute Query")
            print(e)
            sys.exit(1)

        MainMenu.mainMenu().mainMenuOptions()

    def displayCart(self):

        cur = createDatabaseConnection.getDatabaseConnection().createConnection()

        try:
            cur.execute("create table if not exists Cart(productId varchar)")
        except psycopg2.Error as e:
            print("Could Not create table Cart")
            print(e)
            sys.exit(1)

        try:
            Query = "select * from cart"
            cur.execute(Query)
            rec = cur.fetchall()
            if len(rec) != 0:
                print("Product Available in Cart Are:-")
                for product_id in rec:
                    productid = product_id[0]
                    Query = "select * from products where product_id=%s"
                    cur.execute(Query, productid)
                    record = cur.fetchall()[0]
                    print("--------------------------------------------")
                    print("Product id - ", record[0])
                    print("Product Name - ", record[1])
                    print("Price - ", record[2])
                    print("Quantity Available - ", record[3])
                    print("Description - ", record[4])
                    print("Category Id - ", record[5])
                    print("-------------------------------------------")

        except psycopg2.Error as e:
            print("Could Not create table Cart")
            print(e)
            sys.exit(1)

        if len(rec) == 0:
            print("Cart is empty")

        print("1-Proceed to buy")
        print("2-Remove product from Cart")
        print("3-Move to main menu")
        print("4-Move Product to WishList")
        choice = input()
        if choice == '1':
            if len(rec) == 0:
                print("Cart is Empty Moving to Main Menu")
                MainMenu.mainMenu().mainMenuOptions()
            else:
                self.proceedToBuy()
        elif choice == '3':
            MainMenu.mainMenu().mainMenuOptions()
        elif choice == '2':
            if len(rec) == 0:
                print("Cart is Empty Moving to Main Menu")
                MainMenu.mainMenu().mainMenuOptions()
            else:
                self.deleteFromCart()
        elif choice == '4':
            if len(rec) == 0:
                print("Cart is Empty Moving to Main Menu")
                MainMenu.mainMenu().mainMenuOptions()
            else:
                self.moveToWishList()
        else:
            print("Invalid Operation! Moving to Main Menu")
            MainMenu.mainMenu().mainMenuOptions()

    def moveToWishList(self):

        cur = createDatabaseConnection.getDatabaseConnection().createConnection()

        try:
            cur.execute("create table if not exists wishlist(productId varchar)")
        except psycopg2.Error as e:
            print("Could Not create table WishList")
            print(e)
            sys.exit(1)

        try:
            print("Enter the product id that you want to move to wishlist")
            productid = input()
            Query = "select * from cart where productid = %s"
            cur.execute(Query, productid)
            rec = cur.fetchall()
            if len(rec) != 0:
                wishlist_insert_query = """INSERT INTO wishlist(productId) VALUES (%s) """
                insertRecord = (productid)
                cur.execute(wishlist_insert_query, insertRecord)
                sql_delete_query = """Delete from cart where productid = %s"""
                cur.execute(sql_delete_query, productid)
                print("Product Successfully Added to the wishlist and removed from cart")
            else:
                print("The entered product is not available in Cart")

        except psycopg2.Error as e:
            print(e)

        MainMenu.mainMenu().mainMenuOptions()

    def proceedToBuy(self):

        print("Select Payment Option")
        print("1-Credit Card or Debit Card")
        print("2-Internet Banking")
        print("3-Pay on Delivery")
        print("4-Amazon Wallet")
        choice = input()
        if choice == '1':
            paymentMode = "Credit Card or Debit Card"
        elif choice == '2':
            paymentMode = "Internet Banking"
        elif choice == '3':
            paymentMode = "Pay on Delivery"
        elif choice == '4':
            paymentMode = "Amazon Wallet"
        pass
        randomOrderNumber = random.choice([1, 2, 3, 4, 5]) + random.choice([1, 2, 3, 4, 5]) + random.choice(
            [1, 2, 3, 4, 5]) + random.choice([1, 2, 3, 4, 5]) + random.choice([1, 2, 3, 4, 5])
        orderid = "ORD" + str(randomOrderNumber)
        print("Please provide your mobile number")
        mobilenumber = input()
        print("please provide address where order will be shipped")
        address = input()

        cur = createDatabaseConnection.getDatabaseConnection().createConnection()


        try:
            Query = "select * from cart"
            cur.execute(Query)
            rec = cur.fetchall()
            for product_id in rec:
                productid = product_id[0]
                Query = "select * from products where product_id=%s"
                cur.execute(Query, productid)
                record = cur.fetchall()[0]
                orders_insert_query = """INSERT INTO orders (orderid,product_id,mobileNumber,address,price,
                            modeOfPayment) VALUES (%s,%s,%s,%s,%s,%s) """
                insertRecord = (orderid, productid, mobilenumber, address, record[2], paymentMode)
                cur.execute(orders_insert_query, insertRecord)
            print("Order Placed")
            cart_drop_query = "drop table cart"
            cur.execute(cart_drop_query)
        except psycopg2.Error as e:
            print(e)
        print("Order Placed you can check the order status")
        print("Do you want to continue shopping")
        continueShopping = input()
        if continueShopping == 'yes':
            MainMenu.mainMenu().mainMenuOptions()
        elif continueShopping == 'no':
            sys.exit(1)
        else:
            print("Invalid Operation Entered Moving to main menu")
            MainMenu.mainMenu().mainMenuOptions()
