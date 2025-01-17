from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB URI if different
db = client['portfolio']  # Database name
cont_collection = db['person']  # Collection name