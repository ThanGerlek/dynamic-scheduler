import dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

dotenv.load_dotenv()

db_user = dotenv.get_key(".env", "MONGO_DB_USER")
db_password = dotenv.get_key(".env", "MONGO_DB_PASSWORD")

db_name = "scheduler"
db_schedules_collection_name = "schedules"
db_users_collection_name = "users"

uri = (f"mongodb+srv://{db_user}:{db_password}@cluster0.xa2n3tq.mongodb.net/?retryWrites=true&w=majority&appName"
       f"=Cluster0")


class DbDao:
    def __init__(self):
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        self.db = client.get_database(db_name)
        self.schedules = self.db.get_collection(db_schedules_collection_name)
        self.users = self.db.get_collection(db_users_collection_name)

    def get_user_data(self, username: str):
        cursor = self.users.find({"username": username})
        return cursor.to_list()

    def create_user(self, username: str):
        user_data = {"username": username, "schedules": []}
        self.users.insert_one(user_data)

    def clear_user_data(self):
        self.users.delete_many({})
