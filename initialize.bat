@echo off "initializing project"
python -m venv env
@REM if you don't want to restart your ide run the following command otherwise ignore
env\Scripts\activate.bat
pip install -r requirements.txt
django-admin startproject app app
django-admin startproject todo-list .
virtualenv venv
@REM python manage.py runserver 0.0.0.0:8000
@REM python manage.py test
@REM python manage.py startapp core
@REM if we change the model we need to run the migrations again
@REM python manage.py makemigrations core
cd app