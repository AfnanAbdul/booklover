import pandas as pd
class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        # optional attributes
        self.num_books = num_books
        if book_list is None:
            self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        else:
            self.book_list = book_list
        
    def add_book(self, book_name, book_rating):
        '''
        This function takes a book name (string) and rating (integer from 0 to 5)
        '''
        # check if the book to be added is already in the list,
        # only add if the book doesn't already exist
        if book_name in self.book_list['book_name'].tolist(): # convert Pandas Series to list
            print(f"The book {book_name} already exists in your list!")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].tolist()
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    
    
if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Jane Eyre", 4)
    test_object.add_book("Fight Club", 3)
    test_object.add_book("The Divine Comedy", 5)
    test_object.add_book("The Popol Vuh", 2)
    
    print('Has read Fight Club:', test_object.has_read('Fight Club'))
    print('Has read Thinking Fast & Slow:', test_object.has_read('Thinking Fast & Slow'))
    print('Total number of books read:', test_object.num_books_read())
    print('Favorite books:\n', test_object.fav_books())