import MainMenu
import sys
import createDatabaseConnection
import psycopg2
import random


class OrderProduct:

    def buyProduct(self):
        paymentMode = ""
        print("Please provide the Id of product to buy")
        productId = input()
        print("Select Payment Option")
        print("1-Credit Card or Debit Card")
        print("2-Internet Banking")
        print("3-Pay on Delivery")
        print("4-Amazon Wallet")
        paymentChoice = input()
        if paymentChoice == '1':
            paymentMode = "Credit Card or Debit Card"
        elif paymentChoice == '2':
            paymentMode = "Internet Banking"
        elif paymentChoice == '3':
            paymentMode = "Pay on Delivery"
        elif paymentChoice == '4':
            paymentMode = "Amazon Wallet"
        print("Please Provide Address")
        address = input()
        print("Enter your mobile number")
        mobileNumber = input()
        randomOrderNumber = random.choice([1, 2, 3, 4, 5]) + random.choice([1, 2, 3, 4, 5]) + random.choice(
            [1, 2, 3, 4, 5]) + random.choice([1, 2, 3, 4, 5]) + random.choice([1, 2, 3, 4, 5])
        orderid = "ORD" + str(randomOrderNumber)

        cur = createDatabaseConnection.getDatabaseConnection().createConnection()

        try:

            cur.execute("create table if not exists orders(orderid varchar,product_id varchar,mobileNumber varchar,"
                        "address varchar,price int,modeOfPayment varchar);")
        except psycopg2.Error as e:
            print("Could Not create table orders")
            print(e)
            sys.exit(1)

        try:
            Query = "select price from products where product_id=%s"
            cur.execute(Query, (productId,))
            price = cur.fetchall()[0][0]
            orders_insert_query = """INSERT INTO orders (orderid,product_id,mobileNumber,address,price,
            modeOfPayment) VALUES (%s,%s,%s,%s,%s,%s) """
            insertRecord = (orderid, productId, mobileNumber, address, price, paymentMode)
            cur.execute(orders_insert_query, insertRecord)
        except psycopg2.Error as e:
            print("Error Occured while inserting value in database")
            print(e)
            sys.exit(1)

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
