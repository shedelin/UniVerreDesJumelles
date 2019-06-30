from document import Database
from bson.objectid import ObjectId

Md      = Database.MongoDatabase()
db      = Md.db
dbCarts = db.Carts

class Cart:
	_articles   = []
	_totalPrice = 0.0
	_userName   = ''

	def __init__(self, cart_id=None):
		if None == cart_id:
			self.new_cart = True
		else:
			self._id      = ObjectId(cart_id)
			self.new_cart = False

			self._populate()

	def commit(self):
		if self.new_cart:
			dbCarts.insert({
				'articles':   self._articles,
				'totalPrice': self._totalPrice,
				'userName':   self._userName,
			})
			self._id = dbCarts.find_one({'userName': self._userName})['_id']
		else:
			dbCarts.update({'_id': ObjectId(self._id)}, {
				'articles':   self._articles,
				'totalPrice': self._totalPrice,
				'userName':   self._userName,
			})

	def _populate(self):
		cart             = dbCarts.find_one({'_id': ObjectId(self._id)})
		self._articles   = cart['articles']
		self._totalPrice = cart['totalPrice']
		self._userName   = cart['userName']

	def getId(self):
		return str(self._id)

	def toArray(self):
		result = {
			'_id':        self.getId(),
			'articles':   self._articles,
			'totalPrice': self._totalPrice,
			'userName':   self._userName,
		}

		return result

	def addArticle(self, articles):
		if articles._id not in self._articles:
			self._articles.append(articles._id)

	def removeArticle(self, articles):
		self._articles.remove(articles._id)
