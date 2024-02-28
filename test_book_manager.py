import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        # Add setup for test books here
        self.book1 = {'isbn': 1, 'title': 'Book One', 'author': 'Author A'}
        self.book2 = {'isbn': 2, 'title': 'Book Two', 'author': 'Author B'}

    # Implement test methods here
    def test_add_and_list_books(self):
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        self.assertEqual(self.manager.list_books(), {self.book1, self.book2}

    def test_remove_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book('Book One')
        self.assertEqual(self.manager.list_books(), [])

    def test_remove_nonexistent_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book('Nonexistent Book')
        self.assertEqual(self.manager.list_books(), [self.book1])

if __name__ == '__main__':
    unittest.main()
