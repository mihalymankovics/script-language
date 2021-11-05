from pymongo import MongoClient


def get_collection():
    USERNAME = 'root'
    PASSWORD = 'example'
    DB_NAME = 'sample'
    HOST = 'localhost'
    PORT = 27017
    CONNECTION_STRING = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?authSource=admin'
    client = MongoClient(CONNECTION_STRING)
    return client[DB_NAME]['jobs']