from .settings_common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v*qs^ut-7ueqvay+6x25pqz8so^ofakg5*5xdgnmcv2&e4%ji9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['your_domain.com', '127.0.0.1', 'localhost']

# ロギング設定
LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,

  # ロガーの設定
  'loggers': {
    # Djangoが利用するロガー
    'django': {
      'handlers': ['console'],
      'level': 'INFO',
    },
    # diaryアプリケーションが利用するロガー
    'diary': {
      'handlers': ['console'],
      'level': 'DEBUG',
    },
  },

  # ハンドラの設定
  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
      'formatter': 'dev',
    },
  },

  # フォーマッタの設定
  'formatters': {
    'dev': {
      'format': '\t'.join([
        '%(asctime)s',
        '[%(levelname)s]',
        '%(pathname)s(Line:%(lineno)d)',
        '%(message)s',
      ]),
    },
  }
}


# メール配信先をコンソールへ設定
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
