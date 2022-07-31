import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY_ID = os.getenv('Access-key-id')
SECRET_ACCESS_KEY = os.getenv('Secret-access-key')
