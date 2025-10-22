"""
A module representing database models for authors and books.

This module defines SQLAlchemy ORM models for managing authors and books
in a relational database. Authors are represented as a separate entity
with their respective attributes, while books are linked to authors via
a foreign key.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    """
    Represents an author in the database.

    This class is used to define the schema of the "Author" table in the database,
    along with providing utility methods for representation. The class includes
    attributes for storing the author's name, birth date, and date of death.

    :ivar id: Unique identifier for the author, acts as the primary key.
    :type id: int
    :ivar name: Name of the author. It cannot be null.
    :type name: str
    :ivar birth_date: Birth date of the author.
    :type birth_date: datetime.date
    :ivar date_of_death: Date of death of the author, if applicable.
    :type date_of_death: datetime.date
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)

    def __repr__(self):
        return f'<Author {self.name}>'

    def __str__(self):
        return self.name


class Book(db.Model):
    """
    Represents a Book entity in the database.

    This class is used to model a book with attributes such as ISBN, title,
    publication year, and a reference to the author. It provides basic
    information and supports database operations using SQLAlchemy.

    :ivar id: The unique identifier of the book in the database.
    :type id: int
    :ivar isbn: The International Standard Book Number (ISBN) of the book,
        limited to 13 characters.
    :type isbn: str
    :ivar title: The title of the book, limited to 250 characters.
    :type title: str
    :ivar publication_year: The year the book was published.
    :type publication_year: int
    :ivar author_id: The foreign key referencing the unique identifier of the
        related author in the database.
    :type author_id: int
    """
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

    def __str__(self):
        return self.title
