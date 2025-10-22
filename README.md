# Book Alchemy

A Flask web application for managing a library database system. This application provides a user-friendly interface for
managing books and authors, featuring search capabilities and integration with OpenLibrary for book covers.

## Features

- Author Management:
    - Add new authors with biographical information
    - Track birth dates and dates of death
- Book Management:
    - Add new books with ISBN, title, and publication year
    - Link books to authors
    - Display book covers from OpenLibrary API
- Search and Sort:
    - Search books by title or author name
    - Sort book list by title or author
    - Dynamic filtering of results
- User Interface:
    - Clean and responsive design
    - Easy navigation between features
    - Form validation for data entry

## Database Schema

### Authors Table

- id (Primary Key)
- name
- birth_date
- date_of_death

### Books Table

- isbn (Primary Key)
- title
- publication_year
- author_id (Foreign Key)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/book-alchemy.git
   cd book-alchemy
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy
   ```

4. Initialize the database:
   ```bash
   python
   >>> from app import app, db
   >>> with app.app_context():
   ...     db.create_all()
   ```

## API Endpoints

- `GET /`: Home page displaying all books
- `GET /search`: Search books by title or author
- `GET /sort_by_title`: Display books sorted by title
- `GET /sort_by_author`: Display books sorted by author name
- `GET/POST /add_author`: Add new author to database
- `GET/POST /add_book`: Add new book to database

## Usage Examples

### Adding an Author
1. Navigate to "Add Author" from the home page
2. Fill in the author's name (required)
3. Optionally add birth date and date of death
4. Click "Add Author" to save

### Adding a Book
1. Navigate to "Add Book" from the home page
2. Enter the ISBN, title, and publication year
3. Select an author from the dropdown menu
4. Click "Add Book" to save

### Searching for Books
1. Use the search bar on the home page
2. Enter a book title or author name
3. Results will display matching books dynamically

### Sorting Books
- Click "Sort by Title" to arrange books alphabetically by title
- Click "Sort by Author" to arrange books by author name

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a Pull Request

## Known Issues

- Book covers may not display if the ISBN is not found in the OpenLibrary database
- Date validation is basic and may accept invalid dates

## Future Enhancements

- [ ] Book deletion and editing capabilities
- [ ] Author profile pages with full bibliography
- [ ] Advanced search filters (by year, ISBN range, etc.)
- [ ] User authentication and personal reading lists
- [ ] Book ratings and reviews
- [ ] Export library data to CSV/JSON
- [ ] Pagination for large book collections
- [ ] Multiple author support per book

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or suggestions, please open an issue in the GitHub repository.

## Acknowledgments

- Book cover images provided by [OpenLibrary API](https://openlibrary.org/developers/api)
- Built with [Flask](https://flask.palletsprojects.com/) framework
- Database management powered by [SQLAlchemy](https://www.sqlalchemy.org/)
