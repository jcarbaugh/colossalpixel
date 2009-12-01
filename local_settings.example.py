import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
    ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

DATABASE_ENGINE = ''
DATABASE_NAME = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)