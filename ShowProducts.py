import pandas as pd
import psycopg2
import MainMenu
import createDatabaseConnection
import PlaceOrder
import CartOperation
import WishListOperation
import yaml


class showProducts:

    def showAvailableProducts(self):

        with open("config.yaml", 'r') as f:
            config = yaml.safe_load(f)
        host = config['Postgres']['host']
        dbname = config['Postgres']['dbname']
        user = config['Postgres']['user']
        password = config['Postgres']['password']

        try:
            conn = psycopg2.connect(
                host=host,
                database=dbname,
                user=user,
                password=password
            )
        except psycopg2.Error as e:
            print("Error:Could Not make connection to postgresDatabase")
            return e


        try:
            conn.set_session(autocommit=True)
            cur = conn.cursor()
        except psycopg2.Error as e:
            print("Error:Could not get cursor to database")
            print(e)

        try:
            cur.execute("select * from products")
        except psycopg2.Error as e:
            print(e)

        records = cur.fetchall()
        pd.set_option('display.expand_frame_repr', False)
        print(pd.read_sql("select * from products", conn))
        print("Select any option below")
        print("1-Buy the Product")
        print("2-Add to Cart")
        print("3-Add to Wishlist")
        print("4-Return to Main Menu")
        print("Enter any of the option mentioned above")
        choice = input()
        if choice == '1':
            PlaceOrder.OrderProduct().buyProduct()
            pass
        elif choice == '2':
            CartOperation.Cart().addToCart()
            pass
        elif choice == '3':
            WishListOperation.wishList().addToWishList()
            pass
        elif choice == '4':
            MainMenu.mainMenu().mainMenuOptions()



