from document import Database
from bson.objectid import ObjectId

Md      = Database.MongoDatabase()
db      = Md.db
dbUsers = db.Users

class User:
	_cart     = None
	_commands = []
	_email    = ''
	_password = ''
	_right    = ''

	def __init__(self, user_id=None):
		if None == user_id:
			self.new_user = True
		else:
			self._id      = ObjectId(user_id)
			self.new_user = False

			self._populate()

	def commit(self):
		if self.new_user:
			dbUsers.insert({
				'cart':     self._cart,
				'commands': self._commands,
				'email':    self._email,
				'password': self._password,
				'right':    self._right,
			})
			self._id = dbUsers.find_one({'email': self._email})['_id']
		else:
			dbUsers.update({'_id': ObjectId(self._id)}, {
				'cart':     self._cart,
				'commands': self._commands,
				'email':    self._email,
				'password': self._password,
				'right':    self._right,
			})

	def _populate(self):
		user           = dbUsers.find_one({'_id': ObjectId(self._id)})
		self._cart     = user['cart']
		self._commands = user['commands']
		self._email    = user['email']
		self._password = user['password']
		self._right    = user['right']

	def getId(self):
		return str(self._id)

	def toArray(self):
		result = {
			'_id':      self.getId(),
			'cart':     self._cart,
			'commands': self._cards,
			'email':    self._email,
			'right':    self._right,
		}

		return result

	def addCommand(self, commands):
		if commands._id not in self._commands:
			self._commands.append(commands._id)

	def removeCommand(self, commands):
		self._commands.remove(commands._id)
