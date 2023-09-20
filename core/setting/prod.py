from core.settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2a5yhd!&fqiz4ve*n@&9i$sdxr+57m%hk9z8u#hy22xt2=b(z_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["kasratorabi.com","www.kasratorabi.com"]

#sites_id framework for SEO:
SITE_ID = 2

#Rootings
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
