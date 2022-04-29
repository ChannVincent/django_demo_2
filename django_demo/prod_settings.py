from .settings import *
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = False

SECRET_KEY = "9gj7-td73ktyb7q5jt6-sx#4=vbza2&9r^u2o9zzk@c1g2e7^b"

ALLOWED_HOSTS = ["vincent-demo-2.herokuapp.com"]

DATABASES = {"default": dj_database_url.config()}
