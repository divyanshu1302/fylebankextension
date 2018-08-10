import os
from pymongo import MongoClient

from bank_manager.application import app

DATABASE_URI = ''

DATABASE = MongoClient(DATABASE_URI)
db = DATABASE.get_default_database()

BANK_COLLECTION = db.bank
