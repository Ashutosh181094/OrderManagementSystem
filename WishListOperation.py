import sys
import createDatabaseConnection
import psycopg2
import MainMenu


class wishList:

    def addToWishList(self):

        cur = createDatabaseConnection.getDatabaseConnection().createConnection()

        try:
            cur.execute("create table if not exists wishlist(productId varchar)")
        except psycopg2.Error as e:
            print("Could Not create table wishlist")
            print(e)
            sys.exit(1)

        try:
            print("Please provide the Id of product for Adding to wishlist")
            productId = input()
            cart_insert_query = """INSERT INTO wishlist(productId) VALUES (%s) """
            insertRecord = (productId)
            cur.execute(cart_insert_query, insertRecord)
            print("Product Successfully Added to the wishlist")
        except psycopg2.Error as e:
            print("Error Occured while inserting value in database")
            print(e)
            sys.exit(1)
        print("Select Next Operation")
        print("1-Display wishlist")
        print("2-Move items to Cart")
        print("3-Remove from WishList")
        print("4-Move to Main Menu")
        choice = input()
        if choice == '1':
            self.displayWishList()
        elif choice == '2':
            self.moveFromWishListToCart()
        elif choice == '3':
            self.removeFromWishList()
        elif choice == '4':
            MainMenu.mainMenu().mainMenuOptions()
        else:
            print("Incorrect Option Entered Moving you to Main Menu")
            MainMenu.mainMenu().mainMenuOptions()

    def removeFromWishList(self):

        print("Please provide the product Id that you want to remove from wishlist")
        product_id = input()

        cur = createDatabaseConnection.getDatabaseConnection().createConnection()

        try:
            sql_delete_query = """Delete from wishlist where productid = %s"""
            cur.execute(sql_delete_query, product_id)
            print("Product Successfully removed from WishList")
        except psycopg2.Error as e:
            print("Could Not execute Query")
            print(e)
            sys.exit(1)

        MainMenu.mainMenu().mainMenuOptions()

    def displayWishList(self):

        cur = createDatabaseConnection.getDatabaseConnection().createConnection()

        try:
            cur.execute("create table if not exists wishlist(productId varchar)")
        except psycopg2.Error as e:
            print("Could Not create table wishlist")
            print(e)
            sys.exit(1)

        try:
            Query = "select * from wishlist"
            cur.execute(Query)
            rec = cur.fetchall()
            if len(rec) != 0:
                print("Product Available in WishList Are:-")
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
            print("Your WishList is Empty")

        print("1-Remove product from WishList")
        print("2-Move to main menu")
        print("3-Move product from wishlist to cart")
        choice = input()
        if choice == '1':
            if len(rec) != 0:
                self.removeFromWishList()
            else:
                print("Wishlist is empy! Moving to Main Menu")
                MainMenu.mainMenu().mainMenuOptions()
        elif choice == '2':
            MainMenu.mainMenu().mainMenuOptions()
        elif choice == '3':
            if len(rec) != 0:
                self.moveFromWishListToCart()
            else:
                print("Wishlist is empy! Moving to Main Menu")
            MainMenu.mainMenu().mainMenuOptions()
        else:
            MainMenu.mainMenu().mainMenuOptions()

    def moveFromWishListToCart(self):

        cur = createDatabaseConnection.getDatabaseConnection().createConnection()

        try:
            cur.execute("create table if not exists cart(productId varchar)")
        except psycopg2.Error as e:
            print("Could Not create table cart")
            print(e)
            sys.exit(1)

        try:
            print("Enter the product id that you want to move to cart")
            productid = input()
            Query = "select * from wishlist where productid = %s"
            cur.execute(Query, productid)
            rec = cur.fetchall()
            if len(rec) != 0:
                wishlist_insert_query = """INSERT INTO cart(productId) VALUES (%s) """
                insertRecord = (productid)
                cur.execute(wishlist_insert_query, insertRecord)
                sql_delete_query = """Delete from wishlist where productid = %s"""
                cur.execute(sql_delete_query, productid)
                print("Product Successfully Added to the cart and removed from wishlist")
            else:
                print("Entered Product id is not available in Wishlist")

        except psycopg2.Error as e:
            print(e)

        MainMenu.mainMenu().mainMenuOptions()
