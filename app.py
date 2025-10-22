import os
from datetime import datetime

from flask import Flask, render_template, request

from data_models import db, Author, Book

# Initialize flask app
app = Flask(__name__)

# Initialize database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

# Connect database to flask app
db.init_app(app)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        # Get data from form
        name = request.form['name']
        birth_date = datetime.strptime(request.form['birthdate'], '%Y-%m-%d').date()
        try:
            date_of_death = datetime.strptime(request.form['date_of_death'], '%Y-%m-%d').date()
        except ValueError:
            date_of_death = None

        # Add data to database
        author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)
        db.session.add(author)
        db.session.commit()
        return f"Author {name} added successfully!"

    else:
        return render_template("add_author.html")


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Get data from form
        isbn = request.form['isbn']
        title = request.form['title']
        publication_year = request.form['publication_year']
        author_id = request.form['author_id']

        # Add data to database
        book = Book(isbn=isbn, title=title, publication_year=publication_year, author_id=author_id)
        db.session.add(book)
        db.session.commit()
        return f"Book {title} added successfully!"

    else:
        return render_template("add_book.html", authors=Author.query.all())


@app.route('/')
def index():
    books = db.session.query(Book, Author).join(Author).order_by(Book.isbn.desc()).all()
    return render_template("home.html", books=books)


@app.route('/sort_by_title')
def sort_by_title():
    books = db.session.query(Book, Author).join(Author).order_by(Book.title.asc()).all()
    return render_template("home.html", books=books)


@app.route('/sort_by_author')
def sort_by_author():
    books = db.session.query(Book, Author).join(Author).order_by(Author.name.asc()).all()
    return render_template("home.html", books=books)


# Create tables in database
# with app.app_context():
#     db.create_all()
