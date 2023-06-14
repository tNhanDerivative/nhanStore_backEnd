import os
from dotenv import load_dotenv
load_dotenv()


DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1',os.getenv('SERVER_IP')]

CORS_ALLOWED_ORIGINS = [
    os.getenv('CORS_ALLOWED_ORIGINS'),
]