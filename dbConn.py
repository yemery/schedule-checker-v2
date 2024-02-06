from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

def conn_db():
    try:   
        client = MongoClient(os.getenv("MongoDB_URI"))
        db = client[os.getenv("db_name")]

        return db
    except Exception as e:
            print(f"Error : {e}")
            return None