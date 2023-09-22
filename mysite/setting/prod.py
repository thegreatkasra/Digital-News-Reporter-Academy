from mysite.settings import *
import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2a5yhd!&fqiz4ve*n@&9i$sdxr+57m%hk9z8u#hy22xt2=b(z_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["kasratorabi.com","www.kasratorabi.com"]

#sites_id framework for SEO:
SITE_ID = 2

#Rootings
STATICFILES_DIRS = [
    os.path. join (BASE_DIR, 'statics')
]

STATIC_ROOT = '/home/??????/public_html/static'
MEDIA_ROOT = '/home/??????/public_html/media'
STATIC_URL = 'static/'
MEDIA_URL = 'media/'


# Set SECURE_HSTS_SECONDS to the desired duration in seconds
SECURE_HSTS_SECONDS = 31536000  # For example, 1 year

# Additional HSTS settings (optional)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Enforce HSTS on subdomains as well
SECURE_HSTS_PRELOAD = True  # Include your site in HSTS preload lists

