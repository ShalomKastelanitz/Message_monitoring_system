import pymongo


mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["email_monitoring"]
mongo_collection = mongo_db["all_messages"]


