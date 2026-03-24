
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://upasanap004_db_user:Pass2026@cluster0.ap3dgxm.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)