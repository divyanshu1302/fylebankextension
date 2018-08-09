import os
from pymongo import MongoClient

from application import app

DATABASE_URI = 'mongodb://fyle:fyle123@ds117422.mlab.com:17422/fylebank'

DATABASE = MongoClient(DATABASE_URI)
db = DATABASE.get_default_database()

BANK_COLLECTION = db.bank
