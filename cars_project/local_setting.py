# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rjwlr@d5&ko0128+g%v0&llhy81j9m7vax1n-_x$j9*-*#g24w'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Allows developers access to the database without pushing it to GitHub
# Created entirely from scratch, move "DATABASES" and "SECURITY_KEY" here

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'letmeinstudent'
    }
}