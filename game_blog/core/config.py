import os

from fastapi.templating import Jinja2Templates

from security_keys import DB_SETTINGS

SECRET_KEY = b"SECRET_KEY"
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://' + DB_SETTINGS['ADMIN'] + ':' + DB_SETTINGS['PASSWORD'] + '@' + DB_SETTINGS['HOST'] + ':' + DB_SETTINGS['PORT'] + '/' + DB_SETTINGS['DB_NAME']
ALEMBIC_SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://' + DB_SETTINGS['ADMIN'] + ':' + DB_SETTINGS['PASSWORD'] + '@' + DB_SETTINGS['HOST'] + ':' + DB_SETTINGS['PORT'] + '/' + DB_SETTINGS['DB_NAME']

templates = Jinja2Templates(directory="templates")

TemplateResponse = templates.TemplateResponse
