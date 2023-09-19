from core.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2a5yhd!&fqiz4ve*n@&9i$sdxr+57m%hk9z8u#hy22xt2=b(z_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

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
    'compressor'
    
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#Rootings
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


#for summernote security
X_FRAME_OPTIONS = 'DENY'    