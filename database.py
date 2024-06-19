from dotenv import load_dotenv
import os

def get_database_cursor():
    load_dotenv()
    db_user = os.getenv("DB_USER")