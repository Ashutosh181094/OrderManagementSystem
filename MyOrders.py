import sys
import psycopg2
import MainMenu
import pandas as pd
import yaml


class myOrders:
    def orders(self):

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
            sys.exit(1)

        try:
            cur.execute("select * from orders")
            records = cur.fetchall()
            pd.set_option('display.expand_frame_repr', False)
            print(pd.read_sql("select * from orders", conn))
        except psycopg2.Error as e:
            print(e)

            records = cur.fetchall()

        MainMenu.mainMenu().mainMenuOptions()
