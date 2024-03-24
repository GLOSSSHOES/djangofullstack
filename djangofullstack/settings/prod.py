import django_on_heroku
from .base import *

# AMAZON S3 SETTINGS
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_DEFAULT_ACL = "public-read"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_LOCATION = "static"
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {"Access-Control-Allow-Origin": "*"}


DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

# HEROKU LOGGINS
DEBUG_PROPAGATE_EXCEPTIONS = True
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "MYAPP": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}

# HEROKU SETTINGS
django_on_heroku.settings(
    locals(), staticfiles=False
)  # Save static code in S3, not in Heroku
# if (
#     "default" in DATABASES.keys()
#     and "OPTIONS" in DATABASES["default"].keys()
#     and "sslmode" in DATABASES["default"]["OPTIONS"]
# ):
#     del DATABASES["default"]["OPTIONS"]["sslmode"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
