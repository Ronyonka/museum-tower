import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_USERNAME = os.environ.get("DB_USERNAME")
DATABASE_PASSWORD= os.environ.get("DB_PASSWORD")
DATABASE_NAME= os.environ.get("DB_NAME")
DATABASE_HOST= os.environ.get("DB_HOST")