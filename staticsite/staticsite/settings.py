import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '...' # must be unique for your project
DEBUG = TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['mysite.com'] # must match your site domains
INSTALLED_APPS = (
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
ROOT_URLCONF = 'staticsite.urls'
WSGI_APPLICATION = 'staticsite.wsgi.application'
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
