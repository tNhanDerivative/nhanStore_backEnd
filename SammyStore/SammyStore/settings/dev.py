import os
from dotenv import load_dotenv
load_dotenv()

DEBUG= False
ALLOWED_HOSTS = ['127.0.0.1','178.128.25.24']

CORS_ALLOWED_ORIGINS = [
    os.getenv('CORS_ALLOWED_ORIGINS'),
]
