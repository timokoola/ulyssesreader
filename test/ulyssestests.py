from bookworm import BookWorm, handle_line
import unittest
import re, string
#class BasicTests(unittest.TestCase):
#    def setUp(self):
#        self.book = BookWorm("pg4300.txt")
#        while not self.book.completed:
#            self.book.traverse_book()
#    def test_first_line(self):
#        self.assertEqual(self.book.tweets[0][3:],"The Project Gutenberg EBook of Ulysses, by James Joyce")

#    def test_100th_line(self):  
#        self.assertEqual(self.book.tweets[101],"The Project Gutenberg EBook of Ulysses, by James Joyce")



#
# Stephen suffered him to pull out and hold up on show by its corner a
#dirty crumpled handkerchief. Buck Mulligan wiped the razorblade neatly.
#Then, gazing over the handkerchief, he said:

import re
regpunct = re.compile("["+string.punctuation+"]+")


class FullBookTests(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.book = BookWorm("pg4300.txt")

    def test_all_words(self):
        while not self.book.completed:
            self.book.traverse_book()
        f = open("pg4300.txt")
        words = f.readlines()
        f.close()
        #words = words.lower()
        self.words = (" ".join([handle_line(l) for l in words])).lower() 
        self.words2 = (" ".join(self.book.tweets)).lower()
        self.words = regpunct.sub(" ",self.words)
        self.words2 = regpunct.sub(" ",self.words2)
        self.assertItemsEqual(self.words.split(),self.words2.split())

    def test_self(self):
        self.book.self_test()

    def test_advances(self):
        loc = self.book.curr_location()
        while not self.book.completed:
            self.book.traverse_book()
            if not self.book.completed:
                self.assertTrue(loc[0] < self.book.curr_location()[0] or loc[1] < self.book.curr_location()[1], "(%d,%d)" % (loc[0],loc[1]))
            loc = self.book.curr_location()

    def test_pyjaum_count(self):
        while not self.book.completed:
            self.book.traverse_book()
        l = [b for b in self.book.tweets if b.find("Pyjaum") != -1]
        self.assertTrue(len(l) == 1)


class SplitTests(unittest.TestCase):
    def setUp(self):
        self.book = BookWorm("test/split.txt")
        while not self.book.completed:
            self.book.traverse_book()

    def test_length(self):
        self.assertEqual(2,len(self.book.tweets))

    def test_buck_mulligan(self):
        self.assertTrue(self.book.tweets[1].startswith("Buck"))

    def test_all_the_words(self):
        regspaces = re.compile("\s+")
        f = open("test/split.txt")
        words = " ".join(f.readlines())
        f.close()
        words = words.lower().strip()
        words = regspaces.sub(" ",words)
        words2 = (" ".join(self.book.tweets)).lower().strip()
        words2 = regspaces.sub(" ",words2)
        self.assertEqual(words,words2)

if __name__ == "__main__":
    unittest.main()
