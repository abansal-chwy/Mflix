from pymongo import MongoClient # this lets us connect to MongoDB
import pymongo
import pprint
import re
from IPython.display import clear_output

client = MongoClient('mongodb://analytics:analytics-password@mflix-shard-00-00-ey6di.mongodb.net:27017,mflix-shard-00-01-ey6di.mongodb.net:27017,mflix-shard-00-02-ey6di.mongodb.net:27017/test?ssl=true&replicaSet=mflix-shard-0&authSource=admin')

filter = {'language':'Korean, English'}

clear_output()
pprint.pprint(list(client.mflix.movies_initial.find(filter)))