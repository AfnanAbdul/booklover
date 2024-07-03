# BookLover

BookLover is a Python package designed for book enthusiasts who want to manage their reading lists and track their progress in an organized way. This package allows you to create, update, and maintain your collection of books with ease.

## Features
* **Initialize a BookLover Profile**: Create a personal profile with your name, email, and favorite genre.
* **Add Books to Your Collection**: Add books to your collection with details like the book's name and your rating (on a scale of 0 to 5). The package ensures that duplicate entries are avoided, keeping your collection clean and organized.
* **Track Books You’ve Read**: Check if a specific book is in your collection, helping you keep track of your reading history effortlessly.
* **Count Total Books Read**: Get the total number of books you've added to your collection, giving you a quick overview of your reading accomplishments.
* **Identify Favorite Books**: Easily list your favorite books—those rated higher than 3—allowing you to quickly recall the best reads from your collection.
  
## Installation

To install the package, use pip:

```bash
pip install booklover
```

You can also clone the repository directly from GitHub:

```bash
git clone https://github.com/AfnanAbdul/booklover.git
```

## Usage

Below are some examples of how to use the BookLover package in your Python code:

### Importing and Initializing

```python
from booklover import BookLover

# Create an instance of BookLover
# Parameters: name, email, favorite genre
book_lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
```

### Adding a Book

```python
# Add a new book to your collection with a name and rating
book_lover.add_book("War of the Worlds", 4)
book_lover.add_book("The Divine Comedy", 5)

# Trying to add the same book again will show a message and not add the duplicate
book_lover.add_book("War of the Worlds", 4)
```

### Checking if a Book is Read

```python
# Check if a specific book has been read
print('Has read Fight Club:', book_lover.has_read('Fight Club'))
print('Has read War of the Worlds:', book_lover.has_read('War of the Worlds'))
```

### Viewing Total Number of Books Read

```python
# Get the total number of books read
print('Total number of books read:', book_lover.num_books_read())
```

### Listing Favorite Books

```python
# List all books with a rating higher than 3
print('Favorite books:\n', book_lover.fav_books())
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
