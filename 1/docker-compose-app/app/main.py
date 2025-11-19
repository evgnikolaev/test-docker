from pymongo import MongoClient
from pprint import pprint

# MONGO_URL = "mongodb://mongo:27017"   - один сервис использует другой сервис.
#                                             !!mongo - это имя сервиса, которое задавали в docker-compose.yml

MONGO_URL = "mongodb://mongo:27017"
client = MongoClient(MONGO_URL)
db = client.admin
dbs_list = db.command("listDatabases")
pprint(dbs_list)

print("end")