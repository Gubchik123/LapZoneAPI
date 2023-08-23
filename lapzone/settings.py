import os
from pathlib import Path

from dotenv import load_dotenv
from corsheaders.defaults import default_headers
from django.contrib.messages import constants as messages


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = str(os.getenv("SECRET_KEY"))

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third-party apps
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "oauth2_provider",
    "social_django",
    "drf_social_oauth2",
    "ckeditor",
    "ckeditor_uploader",
    "django_filters",
    "drf_yasg",
    "corsheaders",
    # My apps
    "shop.apps.ShopConfig",
    "cart.apps.CartConfig",
    "order.apps.OrderConfig",
    "customer.apps.CustomerConfig",
    "mailing.apps.MailingConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lapzone.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": [BASE_DIR / "templates"],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "lapzone.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "PORT": int(os.getenv("DB_PORT")),
        "HOST": str(os.getenv("DB_HOST")),
        "NAME": str(os.getenv("DB_NAME")),
        "USER": str(os.getenv("DB_USER")),
        "PASSWORD": str(os.getenv("DB_PASSWORD")),
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Kiev"

USE_I18N = False

USE_TZ = True

STATIC_URL = "static/"
STATIC_DIR = BASE_DIR / "static"
STATICFILES_DIRS = [STATIC_DIR]
# STATIC_ROOT = BASE_DIR / "static"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

MESSAGE_TAGS = {messages.INFO: "primary", messages.ERROR: "danger"}

SITE_ID = 1

CART_SESSION_ID = "cart"

ERROR_MESSAGE = "There was an error; please try again later."

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.github.GithubOAuth2",
    "drf_social_oauth2.backends.DjangoOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = str(os.getenv("GOOGLE_OAUTH_CLIENT_ID"))
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = str(os.getenv("GOOGLE_OAUTH_SECRET"))
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]
SOCIAL_AUTH_GITHUB_KEY = str(os.getenv("GITHUB_OAUTH_CLIENT_ID"))
SOCIAL_AUTH_GITHUB_SECRET = str(os.getenv("GITHUB_OAUTH_SECRET"))


REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "drf_social_oauth2.authentication.SocialAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 12,
}

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "#/password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "#/username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "#/activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": False,
    "SERIALIZERS": {},
}

CORS_ORIGIN_WHITELIST = ["http://localhost:5173", "http://127.0.0.1:5173"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{name}: [{asctime}] {levelname} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "formatter": "verbose",
            "class": "logging.StreamHandler",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "general.views": {
            "level": "ERROR",
            "propagate": False,
            "handlers": ["console", "mail_admins"],
        },
    },
}

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_CONFIGS = {
    "default": {
        "skin": "moono",
        "toolbar_YourCustomToolbarConfig": [
            {
                "name": "document",
                "items": [
                    "Preview",
                    "Print",
                ],
            },
            {
                "name": "clipboard",
                "items": [
                    "PasteText",
                    "-",
                    "Undo",
                    "Redo",
                ],
            },
            {
                "name": "editing",
                "items": ["Find", "Replace"],
            },
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "Subscript",
                    "Superscript",
                ],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                ],
            },
            "/",
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
            {
                "name": "insert",
                "items": [
                    "Image",
                    "Youtube",
                    "Flash",
                    "Table",
                    "HorizontalRule",
                    "Smiley",
                    "SpecialChar",
                    "PageBreak",
                    "Iframe",
                ],
            },
            "/",
            {"name": "styles", "items": ["Format", "Font", "FontSize"]},
            {"name": "tools", "items": ["Maximize"]},
        ],
        "toolbar": "YourCustomToolbarConfig",
        "tabSpaces": 4,
        "extraPlugins": ",".join(
            [
                "uploadimage",  # the upload image feature
                # extra plugins
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
                "youtube",
            ]
        ),
    }
}
