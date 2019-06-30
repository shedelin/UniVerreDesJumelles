#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, flash, render_template, url_for, request, session, redirect

from bson.objectid import ObjectId

from document import Database
from document.User import User

import bcrypt
# import sys
# import json

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "super secret key"

Md = Database.MongoDatabase()
db = Md.db

# @app.route('/')
# def index():
# 	if session.get('userid'):
# 		user = User(session.get('userid'))
# 		return  render_template('home.html', user=user.toArray())

# 	flash('successfully logged.')

# 	return redirect(url_for('home'))

@app.route('/login')
def login():
	if request.method == 'POST':
		users      = db.Users
		testedUser = users.find_one({'email' : info['email']})
		if testedUser:
			if bcrypt.hashpw(request.form['pass'].encode('utf-8'), testedUser['password']) == testedUser['password']:
				session['userid'] = str(testedUser['_id'])

				return redirect(url_for('home'))

			flash('bad password')

		flash('username dont exist')

	return redirect(url_for('home'))

	return  render_template('login.html')

@app.route('/logout')
def logout():
	del session['userid']

	return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		users        = db.Users
		existingUser = users.find_one({'email' : info['email']})
		if existingUser is None:
			user          = User()
			hashPass      = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
			user.password = hashPass
			user.email    = request.form['email']

			#insert val in new User
			user.commit()

			session['userid'] = user.getId()

			return redirect(url_for('home'))

		flash('that username already exist')

	return render_template('register.html')

@app.route('/')
def home():
	if session.get('userid'):
		user  = User(session.get('userid'))

		return  render_template('home.html', user=user.toArray())

	return  render_template('home.html')

@app.route('/team')
def team():
	if session.get('userid'):
		user  = User(session.get('userid'))

		return  render_template('team.html', user=user.toArray())

	return  render_template('team.html')

# @app.route('/addcard', methods=['GET', 'POST'])
# def addcard():
# 	if request.method == 'POST' and session.get('userid'):
# 		cardName = request.form['cardname'].capitalize()
# 		cardUrl  = request.form['cardurl']
# 		if not cardUrl and cardName:
# 			flash('you need to set a card name and and url.')

# 			return redirect(url_for('addcard'))

# 		user         = User(session.get('userid'))
# 		dbCard       = db.Cards
# 		existingCard = dbCard.find_one({'name' : request.form['cardname']})
# 		if existingCard is None:
# 			card       = Card()
# 			card._name = cardName
# 			card._link = cardUrl
# 			card._logo = 'alphabet/' + request.form['cardname'][0].lower() + '.png'

# 			#insert val in new Card
# 			card.commit()

# 			user.addCard(card)

# 			#insert card in user
# 			user.commit()

# 			flash('New Card successfuly created added.')

# 			return redirect(url_for('addcard'))

# 		card = Card(existingCard['_id'])

# 		#insert card in user
# 		user.addCard(card)
# 		user.commit()

# 		flash('Card successfuly added.')

# 		return redirect(url_for('home'))

# 	if session.get('userid'):
# 		user = User(session.get('userid'))
# 		return render_template('addcard.html', user=user.toArray())

# 	flash('No user connected.')

# 	return redirect(url_for('home'))

# @app.route('/editcard/<card_id>', methods=['GET', 'POST'])
# def editcard(card_id):
# 	dbCard = db.Cards
# 	card   = Card(card_id)
# 	if card is None:
# 		flash('Card doesnt exist.')

# 		return redirect(url_for('home'))

# 	if request.method == 'POST' and session.get('userid'):
# 		cardName = request.form['cardname'].capitalize()
# 		cardUrl  = request.form['cardurl']
# 		cardLogo = request.form['cardlogo']
# 		if not cardUrl and cardName and cardLogo:
# 			flash('you need to set a card name and url and logo path.')

# 			return redirect(url_for('editcard', card_id=card_id))

# 		card._name = cardName
# 		card._link = cardUrl
# 		card._logo = cardLogo

# 		card.commit()

# 		flash('Card successfuly edited.')

# 		return redirect(url_for('home'))

# 	if session.get('userid'):
# 		user = User(session.get('userid'))
# 		return render_template('editcard.html', user=user.toArray(), card=card.toArray())

# 	flash('No user connected.')

# 	return redirect(url_for('home'))

# @app.route('/removecard/<card_id>', methods=['GET', 'POST'])
# def removecard(card_id):
# 	dbCard = db.Cards
# 	card   = Card(card_id)
# 	if card is None:
# 		flash('Card doesnt exist.')

# 		return redirect(url_for('home'))

# 	if session.get('userid'):
# 		user = User(session.get('userid'))

# 		user.removeCard(card)
# 		user.commit()

# 		flash('Card successfuly removed.')
# 		return redirect(url_for('home'))

# 	flash('No user connected.')

# 	return redirect(url_for('home'))

# if __name__ == '__main__':
#     app.run(debug=True, host=app.config['HOST'], port=8080)

if __name__ == '__main__':
	app.run(debug=True, port=8080)

