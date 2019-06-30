from document import Database
from bson.objectid import ObjectId

Md         = Database.MongoDatabase()
db         = Md.db
dbCommands = db.Commands

class Command:
	_article    = ''
	_deliver    = False
	_payed      = False
	_price      = 0.0
	_userAdress = ''
	_userName   = ''

	def __init__(self, cart_id=None):
		if None == command_id:
			self.new_command = True
		else:
			self._id      = ObjectId(command_id)
			self.new_command = False

			self._populate()

	def commit(self):
		if self.new_command:
			dbCommands.insert({
				'article':    self._article,
				'deliver':    self._deliver,
				'payed':      self._payed,
				'price':      self._price,
				'userAdress': self._articles,
				'userName':   self._userName,
			})
			self._id = dbCommands.find_one({'userName': self._userName})['_id']
		else:
			dbCommands.update({'_id': ObjectId(self._id)}, {
				'article':    self._article,
				'deliver':    self._deliver,
				'payed':      self._payed,
				'price':      self._price,
				'userAdress': self._articles,
				'userName':   self._userName,
			})

	def _populate(self):
		command          = dbCommands.find_one({'_id': ObjectId(self._id)})
		self._article    = command['article']
		self._deliver    = command['deliver']
		self._payed      = command['payed']
		self._price      = command['price']
		self._userAdress = command['userAdress']
		self._userName   = command['userName']

	def getId(self):
		return str(self._id)

	def toArray(self):
		result = {
			'_id':        self.getId(),
			'article':    self._article,
			'deliver':    self._deliver,
			'payed':      self._payed,
			'price':      self._price,
			'userAdress': self._articles,
			'userName':   self._userName,
		}

		return result
