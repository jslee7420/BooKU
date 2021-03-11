from .base import *

ALLOWED_HOSTS = ['13.125.65.219', 'booku.club']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
DEBUG = False
