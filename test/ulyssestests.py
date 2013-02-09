from bookworm import BookWorm
import unittest

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.book = BookWorm("pg4300.txt")
        while not self.book.completed:
            self.book.traverse_book()
    def test_first_line(self):
        self.assertEqual(self.book.tweets[0][3:],"The Project Gutenberg EBook of Ulysses, by James Joyce")

    def test_100th_line(self):  
        self.assertEqual(self.book.tweets[101],"The Project Gutenberg EBook of Ulysses, by James Joyce")

class SplitTests(unittest.TestCase):
    def setUp(self):
        self.book = BookWorm("test/split.txt")
        while not self.book.completed:
            self.book.traverse_book()

    def test_first_line(self):
        self.assertEqual(self.book.tweets[0], """He came over to the gunrest and, thrusting a hand into Stephen's upper pocket, said:""")

    def test_length(self):
        print self.book.tweets
        self.assertEqual(3,len(self.book.tweets))

if __name__ == "__main__":
    unittest.main()
