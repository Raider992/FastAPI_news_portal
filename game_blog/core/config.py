import os
from pathlib import Path
from .img_extension import IMG_EXTENSION_LIST
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from security_keys import DB_SETTINGS

SECRET_KEY = b"SECRET_KEY"
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://' + DB_SETTINGS['ADMIN'] + ':' + DB_SETTINGS['PASSWORD'] + '@' + DB_SETTINGS['HOST'] + ':' + DB_SETTINGS['PORT'] + '/' + DB_SETTINGS['DB_NAME']
ALEMBIC_SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://' + DB_SETTINGS['ADMIN'] + ':' + DB_SETTINGS['PASSWORD'] + '@' + DB_SETTINGS['HOST'] + ':' + DB_SETTINGS['PORT'] + '/' + DB_SETTINGS['DB_NAME']

ROOT_URL = Path(__file__).resolve().parent.parent
MEDIA_URL = os.path.join(ROOT_URL, 'media')
templates = Jinja2Templates(directory="templates")


TemplateResponse = templates.TemplateResponse


mail_conf = ConnectionConfig(
    MAIL_USERNAME='geothermal1234',
    MAIL_PASSWORD="nekipdhjvqknafjk",
    MAIL_FROM="geothermal1234@yandex.ru",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.yandex.ru",
    MAIL_FROM_NAME="Test Messages",
    MAIL_TLS=False,
    MAIL_SSL=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)