import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "techgear_db")

client = MongoClient(MONGO_URI)
database = client[MONGO_DB_NAME]

def get_database():
    return database