import psycopg2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'calc',
        'USER':'postgres',
        'PASSWORD': '1234',
        'HOST':'localhost',
    }
}