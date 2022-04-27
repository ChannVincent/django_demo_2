# install pip

curl https://bootstrap.pypa.io/get-pip.py | python3

# install virtual env

pip install virtualenv

# create virtual env

cd Desktop/
virtualenv env

# activer environnement virtuel

source env/bin/activate

# install django

pip install django

# django-admin

see all django commands

# create project

django-admin startproject django_demo

# run project

cd django_demo/
python3 manage.py runserver

# add app to the project

python3 manage.py startapp appname

# create and update database up to day

python3 manage.py makemigrations (new table)
python3 manage.py migrate

# admin

http://127.0.0.1:8000/admin/

# site

http://127.0.0.1:8000/

# generate user

python3 manage.py createsuperuser
admin (ad@min.com)
admin
