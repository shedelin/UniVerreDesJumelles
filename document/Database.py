from pymongo import MongoClient

class MongoDatabase():

	new = True

	def __init__(self):
		if self.new:
			mongo    = MongoClient('mongodb://steven:stevenpass@cluster0-shard-00-00-z4p9e.mongodb.net:27017,cluster0-shard-00-01-z4p9e.mongodb.net:27017,cluster0-shard-00-02-z4p9e.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')
			self.db  = mongo.jumelle
			self.new = False
