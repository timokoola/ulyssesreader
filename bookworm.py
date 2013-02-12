#!/usr/bin/python
import string
import re



def handle_line(l):
    result = l
    result = result.strip()
    result = result.replace("_","")
    result = result.replace("--","-")
    return result

class BookWorm:
    def __init__(self,filename):
        f = open(filename)
        self.book_array = re.split("\s\s+"," ".join([handle_line(l) for l in f.readlines()]))
        f.close()
        self.reset()

    def reset(self):
        self.cut = 140
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

    def next_part(self,l):
        if len(l) > 0:
            return l[-1]
        else:
            return ""

    def splitters(self):
        s = "\t" + self.to_eol() + "\t"
        lth = len(self.__curr_tweet)
        cut = self.cut
        assert(lth <= cut), "len(%s) = %d > %d" % (self.__curr_tweet, lth, cut)
        result = [l[1]+self.__char for l in zip(s, xrange(len(s))) if l[0] in ",?.!\t" and (lth + l[1]) < (cut-20)]
        # no punctuation during next 120 chars
        if len(result) < 2:
            result = [l[1]+self.__char for l in zip(s, xrange(len(s))) if l[0] in string.whitespace and (lth + l[1]) < cut]
        #special case just one long word
        if len(result) < 2:
            result = [l[1]+self.__char for l in zip(s, xrange(len(s))) if (lth + l[1]) < cut]

        return result

    def to_eol(self):
        return self.book_array[self.__line][self.__char:]

    def split_line(self):
        split = max(self.splitters())
        self.__curr_tweet =  self.__curr_tweet  + self.add_slice(split)
        self.__char = split
        self.store_current()
        if len(re.sub("\s+","",self.to_eol())) == 0:
            self.next_line()

    def add_slice(self,split):
        if split <= self.__char:
            return ""
        else:
            return  " " + self.book_array[self.__line][self.__char:split]
    

    def curr_location(self):
        return (self.__line, self.__char)

    def traverse_book(self):
        # if we are at the end
        if self.__line >= len(self.book_array):
            self.store_current()
            self.completed = True
            return
        if len(self.book_array[self.__line]) == 0:
            self.store_current()
            self.next_line()
        elif len(self.to_eol()) >= 120:
            self.store_current()
            self.split_line()
        else:
            #self.split_line()
            self.__curr_tweet = (" ".join([self.__curr_tweet,self.to_eol()])).strip()
            self.store_current()
            self.next_line()

    def self_test(self):
        if not self.completed:
            while not self.completed:
                self.traverse_book()
        mmx = max(map(len,self.tweets)) 
        assert(mmx <= self.cut)

if __name__ == "__main__":
    bw = BookWorm("pg4300.txt")
    while not bw.completed:
        bw.traverse_book()
    bw.self_test()
