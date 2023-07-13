from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST
from flask_migrate import Migrate


app = Flask(__name__)
db_user = DATABASE_USERNAME
db_password = DATABASE_PASSWORD
db_name = DATABASE_NAME
db_host = DATABASE_HOST

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()