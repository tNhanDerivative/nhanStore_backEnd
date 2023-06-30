
import os
from dotenv import load_dotenv
load_dotenv()


DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1','localhost',os.getenv('SERVER_IP'),  os.getenv('DOMAIN_NAME')]

CORS_ALLOWED_ORIGINS = [
    os.getenv('CORS_ALLOWED_ORIGINS'),
]