from pymongo import MongoClient # this lets us connect to MongoDB
import pymongo
import pprint
from IPython.display import clear_output

client = MongoClient('mongodb://analytics:analytics-password@mflix-shard-00-00-ey6di.mongodb.net:27017,mflix-shard-00-01-ey6di.mongodb.net:27017,mflix-shard-00-02-ey6di.mongodb.net:27017/test?ssl=true&replicaSet=mflix-shard-0&authSource=admin')

"""pipeline = [
    {
        '$group': {
            '_id':{'language':'$language'},
            'count':{'$sum':1}
            }
    },
        {
        '$sort':{'count':-1} #-1 sort in descending order else 1 #sorted on count
            }"""

"""
pipeline = [
    {
        '$match': {'language':'Korean','English'}
        }
        ]
"""
#gives most frequent used combination of lanuages
pipeline = [
    {
        '$sortByCount': '$language'

            },
    {
        '$facet':{
            'top language combinations': [{'$limit':100}],
            'unusual combination shared by':[{
                '$skip':100
            },
                {
                    '$bucketAuto':{
                        'groupBy':"$count",
                        'buckets':5,
                        'output':{
                            'language combinations':{'$sum':1}
                        }
                    }
                }
            ]
        }
    }


]
clear_output()
pprint.pprint(list(client.mflix.movies_initial.aggregate(pipeline)))