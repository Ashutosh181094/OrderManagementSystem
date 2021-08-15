import psycopg2
import yaml
import sys

class getDatabaseConnection:

    def createConnection(self):

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


        return cur






