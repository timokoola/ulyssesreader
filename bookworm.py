#!/usr/bin/python
import re

regsplit = re.compile("([^.?!]+[.!?]) ")

class BookWorm:
    def __init__(self,filename):
        f = open(filename)
        self.book_array = [l.strip() for l in f.readlines()]
        f.close()
        self.__line = 0
        self.__char = 0
        self.location = 0
        self.tweets = []
        self.__curr_tweet = ""
        self.completed = False

    def store_current(self):
        if len(self.__curr_tweet) > 0:
            self.tweets.append(self.__curr_tweet.strip())
        self.__curr_tweet = ""

    def next_line(self):
        self.__line = self.__line + 1
        self.__char = 0

    def split_line(self):
        parts = regsplit.findall(self.book_array[self.__line])
        if len(parts) == 0:
            parts = self.book_array[self.__line].split()
        while len(self.__curr_tweet) != 0:
            added = parts[::-1].pop()
            if len(added) + len(self.__curr_tweet) +1 >= 140:
                self.store_current()
            else:
                self.__char = self.__char + len(added) + 1
                self.__curr_tweet = self.__curr_tweet+ " " + added

    def traverse_book(self):
        # if we are at the end
        if self.__line >= len(self.book_array):
            self.store_current()
            self.completed = True
            return
        if len(self.book_array[self.__line]) == 0:
            self.store_current()
            self.next_line()
        elif len(self.book_array[self.__line]) >= 140:
            self.store_current()
            self.split_line()
        elif len(self.__curr_tweet) + len(self.book_array[self.__line]) >= 140:
            self.split_line()
        else:
            self.__curr_tweet = self.__curr_tweet + " " + self.book_array[self.__line]
            self.next_line()

    def self_test(self):
        if not self.completed:
            while not bw.completed:
                bw.traverse_book()
        mmx = max(map(len,bw.tweets)) 
        assert(mmx < 140)

if __name__ == "__main__":
    bw = BookWorm("pg4300.txt")
    while not bw.completed:
        bw.traverse_book()
    bw.self_test()
