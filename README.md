# ulyssesreader

Ulysses Reader source code is here.

## Pre-requirements

You need to have version 2.7 of Python installed in your system. Test this by opening the command line and writing.

	python

And you should see something like this:

	Python 2.7.2 (default, Oct 11 2012, 20:14:37) 
	[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 

Type in Ctrl-d to exit Python prompt.

## Install Tweepy

Next step is to install Python Tweet library [tweepy](https://github.com/tweepy/tweepy). Install it using [pip Python package manager](https://pypi.python.org/pypi/pip)


## Register Twitter application

Next step is to register a Twitter application for the book reader (this needed so that Ulysessreader can tweet as you). 

1. Go to [Twitter dev site](https://dev.twitter.com/apps)
2. Sign in as you.
3. Select "Create a new application" 
4. Fill in the details (you can ignore callback URL), accept the terms, answer the CAPTCHA and "Create your Twitter application"
5. Application details page opens. 
6. Select "Settings" tab <- THIS IS IMPORTANT
7. Scroll down to "Application type" and select "Read and Write" and push button "Update this Twitter Application's settings". Without this the script is not allowed to tweet on you behalf. <- THIS IS IMPORTANT
8. Click back to details and click button that says "Create my access token". 
9. Make note of following fields for future use:
	* Consumer key
	* Consumer secret
	* Access token
	* Access token secret
10. Re-confirm also that access token "Access level says 'Read and write'". Make sure these keys are safely stored (don't publish them in GitHub for instance).

Congratulations, you now have all the pre-requisites in place.

# Install Ulyssesreader

## Get the source code from GitHub

There are couple of options:
* Download the zip
* Clone the Git repository (If you don't know what that means select the first option)

Put the script into a directory on your system.

## Create "keys.keys" file

Create a file called "keys.keys" into the directory you put the. It should have 4 lines and look like this

	<your consumer key from step 9 above>#consumer key
	<your consumer secret from step 9 above>#consumer secret
	<your access token from step 9 above>#access token
	<your access token secret from step 9 above>#access token secret

Save the file.

## Get the book as a text file

Download whatever you want to tweet in bookform as a text file. This repository contains the full text of Ulysses from Gutenberg project [Ulysses by James Joyce](http://www.gutenberg.org/cache/epub/4300/pg4300.txt)

## Test run ulyssesreader

Ulyssesreader script comes with couple of command line options. Get them by typing 

	python reader.py -h
	usage: reader.py [-h] [-t TEST] [-k KEYFILE] [-b BOOKFILE] [-l LOGFILE]

	Tweets a text format book, line by line.

	optional arguments:
	  -h, --help            show this help message and exit
	  -t TEST, --test TEST  Run a test run, get nth tweet
	  -k KEYFILE, --keyfile KEYFILE
	                        Twitter account consumer and accesstokens
	  -b BOOKFILE, --bookfile BOOKFILE
	                        Book to be read
	  -l LOGFILE, --logfile LOGFILE
	                        File contains ino about Line we are on.

Alternatively you can omit "python" command and call the script like this:

	./reader.py <arguments>

You can now start a book by typing in:

	python reader.py -k keys.keys -b book.txt -l whereweare.txt

This tweets the line 1 of the book and writes "1" to the end of "whereweare.txt" file. This file is used to determine where we are in progress of the book. Run it again to tweet line 2 and so forth. 

	python reader.py -k keys.keys -b book.txt -l whereweare.txt

## Run script in crontab

Crontab is a Unix command (Linux/Mac and so forth) to run commands at regular intervals. I am running my Ulyssesreader with following crontab line:

	8,18,28,38,48,58 * * * * /home/ubuntu/scriptapps/ulyssesreader/reader.py -k /home/ubuntu/scriptapps/ulyssesreader/keys.keys -b /home/ubuntu/scriptapps/ulyssesreader/pg4300.txt -l /home/ubuntu/scriptapps/ulyssesreader/tweetedids.txt

What this says is that script is run 8, 18, 28 minutes after full hour, every hour, every day. Crontab needs full paths to all files and that makes the line so verbose.

You can get more info about crontab by typing:
	man crontab

To add the line above to be executed by crontab type:
	crontab -e

## Notes

This script is free to use whatever way you like. It is licensed under the APACHE LICENSE v2. It isn't particularly smart piece of SW engineering but it gets the job done.

## Notes about the design

Script is not the smartest script around. It is designed to be fool and crash-proof and not to require any external backend and to have minimal dependencies outside the tweepy-library. You can make it work with Python 2.6 by changing the import of argparse (use import from __future__). Script parses the whole book every time so that we can continue where we left of even if we need to change computers on the fly (also it is relatively easy to reconstruct everything from scratch). Only thing that is needed is the source code and the keys-file. Downside of the design is that book must not be changed while tweeting. This throws the location off.


