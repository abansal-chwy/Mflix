from pymongo import MongoClient
client = MongoClient('mongodb://analytics:analytics-password@mflix-shard-00-00-ey6di.mongodb.net:27017,mflix-shard-00-01-ey6di.mongodb.net:27017,mflix-shard-00-02-ey6di.mongodb.net:27017/test?ssl=true&replicaSet=mflix-shard-0&authSource=admin')
print(client.mflix)