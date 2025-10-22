import os

from data_models import db, Author, Book
from flask import Flask

# Initialize flask app
app = Flask(__name__)

# Initialize database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

# Connect database to flask app
db.init_app(app)

# Create tables in database
# with app.app_context():
#  db.create_all()
