# Djando Wednesdays -- Codemy.com

## 01. Before You Install Django...Watch This! #1

* python -m venv virt

* source virt/bin/activate
	** deactivate

* pip freeze

* pip install django==3.1.5

* django-admin startproject myclub_website

* python manage.py runserver

* http://localhost:8000

* python manage.py startapp events




## 02. How To Add A Calendar To Your Website

* http://localhost:8000/2023/January/

* {{ cal | safe }}	### here the safe is a filter.




## 03. How To Use Templates and Custom HTML

* Booststrip



## 04. Using Multiple Database Tables With Django

* http://localhost:8000/admin

* ~ $ winpty python manage.py creatsuperuser
	or: ~$ python manage.py creatsuperuser
* python manage.py migrate

* UserID: Admin  Password: 0915

* 21:29 / 28:41	In directory: myclub_website2
	$ python manage.py makemigrations
	* you would see the follows if you makemigrations successfully.
		Migrations for 'events':
  			events/migrations/0001_initial.py
    			- Create model MyClubUser
    			- Create model Venue
    			- Create model Event

* 23:40 / 28:41	In directory: myclub_website2
	$ python manage.py migrate

	$ python manage.py runserver

## 06. How to Modify the Django Admin Area

## 07. How to Add Database Forms to a Web Page

## 08. How to query the Database for Venues


