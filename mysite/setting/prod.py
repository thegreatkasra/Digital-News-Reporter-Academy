from mysite.settings import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2a5yhd!&fqiz4ve*n@&9i$sdxr+57m%hk9z8u#hy22xt2=b(z_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["kasratorabi.com","www.kasratorabi.com"]

#sites_id framework for SEO:
SITE_ID = 2

# Application definition
INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website.apps.WebsiteConfig',
    'blog',
    'accounts',
    #extentions:
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
    'taggit',
    'django_summernote',
    'captcha',
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'data_base_name',             #edit kon
        'USER': 'user_name',                  #edit kon
        'PASSWORD': 'password of data base',  #edit kon
        'HOST': 'localhost',  
        'PORT': '3306',      
    }
}



#Rootings


STATICFILES_DIRS = [
    os.path. join (BASE_DIR, 'statics')
]

STATIC_ROOT = '/home/???????username of host/public_html/static'
MEDIA_ROOT = '/home/???????username of host/public_html/media'
STATIC_URL = 'static/'
MEDIA_URL = 'media/'


#for summernote security
X_FRAME_OPTIONS = 'DENY'    

# Set SECURE_HSTS_SECONDS to the desired duration in seconds
SECURE_HSTS_SECONDS = 31536000  # For example, 1 year

# Additional HSTS settings (optional)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Enforce HSTS on subdomains as well
SECURE_HSTS_PRELOAD = True  # Include your site in HSTS preload lists
