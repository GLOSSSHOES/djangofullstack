from .base import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"  # is the url where can be seen the static files
STATICFILES_DIRS = [
    BASE_DIR / "static"
]  # is the placement where are located the static files
STATIC_ROOT = BASE_DIR / "staticfiles"  # For NOT DYNAMIC images
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  # For NOT SERVER external deployment

MEDIA_URL = "/media/"  # is the url where can be seen the MEDIA files
MEDIA_ROOT = BASE_DIR / "media"  # For DYNAMIC images
