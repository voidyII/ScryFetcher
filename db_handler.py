import os
import json
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PW   = os.getenv("DB_PW")
DB_NAME = os.getenv("DB_NAME")

mydb = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PW
)

cursor = mydb.cursor()
cursor.execute(f"USE {DB_NAME}")

def dbAdd_bulkDef():
    return

def dbAdd_bulkAll():
    return