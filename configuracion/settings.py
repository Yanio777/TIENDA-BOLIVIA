import os
import dj_database_url  
from pathlib import Path
import cloudinary
import cloudinary.uploader # <-- AÑADIMOS ESTO PARA QUE FUNCIONE EL SUBIDOR
import cloudinary.api

# 1. Rutas
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Seguridad
SECRET_KEY = 'django-insecure-&x!5^r181!rm%@4@l*#091xp7#3!%flj@v2l5vf*_d-wf68+7o'
DEBUG = True
ALLOWED_HOSTS = ['*']

# 3. Aplicaciones
INSTALLED_APPS = [
    'cloudinary_storage', # Primero el almacenamiento
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',         # Luego la librería base
    'catalogo',
]

# 4. Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'configuracion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'configuracion.wsgi.application'

# 5. Base de Datos (PostgreSQL - YA ESTÁ TU URL CORRECTA)
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://tienda_bolivia_db_user:qQaUj0UzRBwyf64J92nQLHP5BomddB92@dpg-d58c37e3jp1c73be2jmg-a/tienda_bolivia_db', 
        conn_max_age=600
    )
}

# 6. Configuración Regional
LANGUAGE_CODE = 'es-bo'
TIME_ZONE = 'America/La_Paz'
USE_I18N = True
USE_TZ = True

# 7. Estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] if os.path.exists(os.path.join(BASE_DIR, 'static')) else []

# 8. Almacenamiento (CORRECCIÓN CLAVE)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dbe8judc6',
    'API_KEY': '957824476582826',
    'API_SECRET': '-aujiF39lV11mpFo_lhBHMJQknc',
}

# CONFIGURACIÓN MANUAL PARA ASEGURAR LA CONEXIÓN
cloudinary.config(
    cloud_name = 'dbe8judc6',
    api_key = '957824476582826',
    api_secret = '-aujiF39lV11mpFo_lhBHMJQknc',
    secure = True
)

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
}

# 9. Multimedia
MEDIA_URL = '/media/'

# 10. Validadores
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'