
from pymongo import MongoClient
from settings.config import Config

client = MongoClient(Config.MONGO_URI)
mongo_db = client[Config.MONGO_DB_NAME]
