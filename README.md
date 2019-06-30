# PROJET JUMELLE

installation:

	installer pip:
	- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	- sudo python get-pip.py

	installer virtualenv:
	- sudo pip install virtualenv

	lancer virtualenv et installer flask: (si souci faite un sudo devant les commandes)
	- virtualenv env -p python3
	- virtualenv env --python=python2.7 (pour passer python en version 2.7.13)
	- . env/bin/activate
	- pip install flask
	- pip install Flask-Pymongo
	- pip install bcrypt
	- pip install dnspython
	- pip install flask_oauth
	- dulpiquer config.py.dist en config.py
	- ajouter les bonnes valeurs dans le config.py

Pour lancer le serveur:
- . env/bin/activate
- python run.py
- lancer: 
