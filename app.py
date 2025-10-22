"""Flask app to manage books and authors."""

import os
from datetime import datetime

import requests
from flask import Flask, render_template, request, redirect, flash
from sqlalchemy import or_

from data_models import db, Author, Book

# Initialize flask app
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Initialize database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

# Connect database to flask app
db.init_app(app)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    """Add author to database."""
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
        flash(f"Author {name} added successfully!", 'success')
        return redirect("/")

    return render_template("add_author.html")


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    """Add book to database."""
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
        flash(f'Book {title} added successfully!', 'success')
        return redirect("/")

    return render_template("add_book.html", authors=Author.query.all())


@app.route('/')
def index():
    """Show all books in database."""
    books = db.session.query(Book, Author).join(Author).order_by(Book.isbn.desc()).all()
    return render_template("home.html", books=books)


@app.route('/sort_by_title')
def sort_by_title():
    """Show all books in database sorted by title."""
    books = db.session.query(Book, Author).join(Author).order_by(Book.title.asc()).all()
    return render_template("home.html", books=books)


@app.route('/sort_by_author')
def sort_by_author():
    """Show all books in database sorted by author."""
    books = db.session.query(Book, Author).join(Author).order_by(Author.name.asc()).all()
    return render_template("home.html", books=books)


@app.route('/search', methods=['GET'])
def search():
    """Search for books in database."""
    query = request.args.get('search', '')

    books = []
    if query:
        books = (
            db.session.query(Book, Author)
            .join(Author)
            .filter(
                or_(
                    Book.title.ilike(f"%{query}%"),
                    Author.name.ilike(f"%{query}%")
                )
            )
            .order_by(Book.isbn.desc())
            .all()
        )
    else:
        flash("Please enter a search query.", 'warning')

    return render_template('home.html', books=books)


@app.route('/book/<int:book_id>/delete', methods=['GET', 'DELETE'])
def delete_book(book_id):
    """Delete book from database."""
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash(f'Book {book.title} deleted successfully!', 'success')
    return redirect("/")


@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """Show details of book in database."""
    book = db.session.query(Book, Author).join(Author).filter(Book.id == book_id).first()
    details = requests.get(f"https://openlibrary.org/search.json", params={
        "isbn": book.Book.isbn,
    }).json()
    return render_template('book_details.html', book=book, details=details)


@app.route('/author/<int:author_id>/delete', methods=['GET', 'DELETE'])
def delete_author(author_id):
    """Delete author from database."""
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()

    books = Book.query.filter(Book.author_id == author_id).all()
    for book in books:
        db.session.delete(book)
        db.session.commit()

    flash(f'Author {author.name} deleted successfully!', 'success')
    return redirect("/")


# Create tables in database
# with app.app_context():
#     db.create_all()
