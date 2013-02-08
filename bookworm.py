#!/usr/bin/python
import re

regsplit = re.compile("([^.?!]+[.!?]) ")


def handle_line(l):
    result = l
    result = result.strip()
    result = result.replace("_","")
    result = result.replace("--","-")
    return result

class BookWorm:
    def __init__(self,filename):
        f = open(filename)
        self.book_array = [handle_line(l) for l in f.readlines()]
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
        cut = 140
        if len(parts) == 0:
            parts = self.book_array[self.__line].split()
            cut = 140
        parts.reverse()
        while len(self.__curr_tweet) != 0 and len(parts) > 0:
            added = parts.pop()
            if len(added) + len(self.__curr_tweet) +1 >= cut:
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
        elif len(self.book_array[self.__line][self.__char:]) >= 140:
            self.store_current()
            self.split_line()
        elif len(self.__curr_tweet) + len(self.book_array[self.__line]) >= 140:
            self.split_line()
        else:
            self.__curr_tweet = self.__curr_tweet + " " + self.book_array[self.__line][self.__char:]
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
