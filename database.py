from dotenv import load_dotenv
import psycopg2
import os


class Database:
    def __init__(self: object):
        print("💾 Database connection opened.")
        load_dotenv()

        self.database_name: str = os.getenv("DATABASE_NAME")
        self.database_user: str = os.getenv("DATABASE_USER")
        self.database_password: str = os.getenv("DATABASE_PASSWORD")
        self.database_host: str = os.getenv("DATABASE_HOST")

        self.database_connection: psycopg2.connect = psycopg2.connect(
            dbname=self.database_name,
            user=self.database_user,
            password=self.database_password,
            host=self.database_host,
        )

        self.database_cursor: psycopg2._psycopg.cursor = (
            self.database_connection.cursor()
        )

    def __del__(self: object):
        self.database_cursor.close()
        self.database_connection.close()
        print("💾 Database connection closed.")
