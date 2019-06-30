from document import Database
from bson.objectid import ObjectId

Md         = Database.MongoDatabase()
db         = Md.db
dbArticles = db.Articles

class Article:
	_name   = ''
	_photo  = ''
	_price  = 0.0
	_color  = ''
	_motif  = ''
	_number = 0

	def __init__(self, article_id=None):
		if None == article_id:
			self.new_article = True
		else:
			self._id         = ObjectId(article_id)
			self.new_article = False

			self._populate()

	def commit(self):
		if self.new_article:
			dbArticles.insert({
				'name':   self._name,
				'photo':  self._photo,
				'price':  self._price,
				'color':  self._color,
				'motif':  self._motif,
				'number': self._number,
			})
			self._id = dbArticles.find_one({'name': self._name})['_id']
		else:
			dbArticles.update({'_id': ObjectId(self._id)}, {
				'name':  self._name,
				'photo': self._photo,
				'price': self._price,
				'color':  self._color,
				'motif':  self._motif,
				'number': self._number,
			})

	def _populate(self):
		article      = dbArticles.find_one({'_id': ObjectId(self._id)})
		self._name   = article['name']
		self._photo  = article['photo']
		self._price  = article['price']
		self._color  = article['color']
		self._motif  = article['motif']
		self._number = article['price']

	def getId(self):
		return str(self._id)

	def toArray(self):
		result = {
			'_id':    self.getId(),
			'name':   self._name,
			'photo':  self._photo,
			'price':  self._price,
			'color':  self._color,
			'motif':  self._motif,
			'number': self._number,
		}

		return result
