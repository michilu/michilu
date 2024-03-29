# -*- coding: utf-8 -*-
from django.conf import global_settings
import os.path
import sys


DEBUG = (False, True)[0]
if os.path.exists("../_debug"):
    DEBUG = (False, True)[1]
TEMPLATE_DEBUG = DEBUG

CUSTOM_DEVELOPMENT = (False, True)[0]
if os.path.exists("../_debug"):
    CUSTOM_DEVELOPMENT = (False, True)[1]

CUSTOM_TEST = False
if sys.argv[0].split("/")[-1] == "manage.py" and sys.argv[1] == "test":
    CUSTOM_TEST = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

PROJECT_PATH = "/data/django/michilu/"
_proj_name = "michilu"
if CUSTOM_DEVELOPMENT:
    PROJECT_PATH = ""
    _proj_name = os.path.split(os.path.abspath(""))[-1]
    #_proj_name = os.path.dirname(os.path.abspath(__file__))
_proj_db = os.path.abspath('%s../db/%s.db' % (PROJECT_PATH, _proj_name))


DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = _proj_db


TIME_ZONE = 'Asia/Tokyo'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True

SERVER_DOMAIN = "http://michilu.com"
_static_domain = SERVER_DOMAIN #+ ":8080"
_static_path = "/static/"

MEDIA_ROOT = PROJECT_PATH + _static_path
if CUSTOM_DEVELOPMENT:
    MEDIA_ROOT = os.path.abspath(".%s" % _static_path)

MEDIA_URL = _static_domain + _static_path
if CUSTOM_DEVELOPMENT:
    MEDIA_URL = _static_path

ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = None

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "michilu.utils.context_processors.context",
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.CacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'michilu.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'templates',
    'helpdoc/templates',
    'blog/templates',
    'doc/templates',
    'demo/templates',
)
TEMPLATE_DIRS = tuple(
    [os.path.abspath("%s%s" % (PROJECT_PATH, _dir)).replace(os.sep, "/") for _dir in TEMPLATE_DIRS]
)

MIME_TYPES = "%sconf/servers/mime.types" % PROJECT_PATH

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
#CACHE_MIDDLEWARE_SECONDS = 10

if CUSTOM_TEST:
    CACHE_BACKEND = 'dummy:///'
    cache = "django.middleware.cache.CacheMiddleware"
    if cache in MIDDLEWARE_CLASSES:
        m = list(MIDDLEWARE_CLASSES)
        m.remove(cache)
        MIDDLEWARE_CLASSES = tuple(m)

CUSTOM_DOC_JA_DIR = os.path.abspath(PROJECT_PATH + "../doc-jp/%s")
CUSTOM_DOC_JA_PATHPATTERN = "%s%s.txt"

CUSTOM_FEED_DATA_path = "static/temp/%s"
if CUSTOM_TEST:
    CUSTOM_FEED_DATA_path = "blog/tests/root/" + CUSTOM_FEED_DATA_path
CUSTOM_FEED_DATA = os.path.abspath(PROJECT_PATH + CUSTOM_FEED_DATA_path)

RESTRUCTUREDTEXT_FILTER_SETTINGS = {
    'doctitle_xform': False,
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.sitemaps',
    'django.contrib.comments',

    'michilu.utils',
    'michilu.helpdoc',
    'michilu.blog',
    'michilu.doc',
    'michilu.offline',
    'michilu.demo',
)

from utils import utils
optional_settings = utils.get_optional_settings("%sconf/settings/settings_overload.py" % PROJECT_PATH)
if optional_settings:
    for key,var in optional_settings.items():
        vars()[key] = var
    if CUSTOM_DEVELOPMENT:
        pass
        #print "#"*10 + " SETTINGS OVERLOADED " + "#"*10
