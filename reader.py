#!/usr/bin/python
#
#   Copyright 2013 Moarub Oy
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import tweepy, sys, os
from collections import Counter
import re
import argparse # requires 2.7
from bookworm import BookWorm

class TweepyHelper:
    def __init__(self,keyfile):
        f = open(keyfile)
        lines = f.readlines()
        f.close()
        consumerkey = lines[0].split("#")[0]
        consumersecret = lines[1].split("#")[0]
        accesstoken = lines[2].split("#")[0]
        accesssec = lines[3].split("#")[0]

        auth = tweepy.OAuthHandler(consumerkey, consumersecret)
        auth.set_access_token(accesstoken, accesssec)
        self.api = tweepy.API(auth)


def handle_command_line():
    parser = argparse.ArgumentParser(description="Tweets a text format book, line by line.")
    parser.add_argument("-t", "--test", help="Run a test run", action="store_true")
    parser.add_argument("-k", "--keyfile", help="Twitter account consumer and accesstokens")
    parser.add_argument("-b", "--bookfile", help="Book to be read")
    args = parser.parse_args()
    return args

def get_tweeted_file():
    try:
        f = open("tweetedids.txt","r+")
    except:
        f = open("tweetedids.txt","w+")
    return (f, f.readlines())


def log_tweeted(tid):
    f, ignred = get_tweeted_file()
    f.write(tid)
    f.write("\n")
    f.close()

if __name__ == "__main__":
    args = handle_command_line()

    api = (TweepyHelper(args.keyfile)).api

    bw = BookWorm("pg4300.txt")
    while not bw.completed:
        bw.traverse_book()
    print bw.tweets
    api.update_status(bw.tweets[1])
