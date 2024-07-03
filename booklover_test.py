from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        # create BookLover instance
        booklover1 = BookLover('Afnan', 'aa7dd@virginia.edu', 'self-help')
        # add books
        book1 = 'the confidence gap'
        booklover1.add_book(book1, 4)
        # Test
        self.assertTrue(book1 in booklover1.book_list['book_name'].values, 'The book should be in the book_list')
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        # create BookLover instance
        booklover1 = BookLover('Afnan', 'aa7dd@virginia.edu', 'self-help')
        # add books
        book1 = 'the confidence gap'
        book2 = 'Letting Go'
        booklover1.add_book(book1, 4)
        booklover1.add_book(book2, 3)
        # add the book1 again
        booklover1.add_book(book1, 5)
        # Test
        expected = 1
        actual = len(booklover1.book_list[booklover1.book_list['book_name'] == book1])
        self.assertEqual(actual, expected, f'the book {book1} should only appear once in the book_list')
        
    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        # create BookLover instance
        booklover1 = BookLover('Afnan', 'aa7dd@virginia.edu', 'self-help')
        # add books
        book1 = 'the confidence gap'
        book2 = 'Letting Go'
        booklover1.add_book(book1, 4)
        booklover1.add_book(book2, 3)
        # Test
        self.assertTrue(booklover1.has_read('Letting Go'))
        
    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        # create BookLover instance
        booklover1 = BookLover('Afnan', 'aa7dd@virginia.edu', 'self-help')
        # add books
        book1 = 'the confidence gap'
        book2 = 'Letting Go'
        booklover1.add_book(book1, 4)
        booklover1.add_book(book2, 3)
        # Test
        self.assertFalse(booklover1.has_read('War of the Worlds'))
        
    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        # create BookLover instance
        booklover1 = BookLover('Afnan', 'aa7dd@virginia.edu', 'self-help')
        # add books
        book1 = 'the confidence gap'
        book2 = 'Letting Go'
        book3 = 'The Untethered Soul'
        booklover1.add_book(book1, 4)
        booklover1.add_book(book2, 3)
        booklover1.add_book(book3, 5)
        # Test
        expected = 3
        self.assertEqual(booklover1.num_books_read(), expected)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        # create BookLover instance
        booklover1 = BookLover('Afnan', 'aa7dd@virginia.edu', 'self-help')
        # add books
        book1 = 'the confidence gap'
        book2 = 'Letting Go'
        book3 = 'The Untethered Soul'
        book4 = 'crucial conversations'
        booklover1.add_book(book1, 4)
        booklover1.add_book(book2, 3)
        booklover1.add_book(book3, 5)
        booklover1.add_book(book4, 2)
        # Test
        fav_books_df = booklover1.fav_books()
        for index, row in fav_books_df.iterrows():
            self.assertGreater(row['book_rating'], 3, f"The book '{row['book_name']}' should have a rating > 3")
        
if __name__ == '__main__':
    unittest.main(verbosity=3)