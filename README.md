# ulyssesreader

Ulysses Reader source code is here.

# Installation

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
10. Re-confirm also that access token "Access level says 'Read and write'"

Congratulations, you now have all the pre-requisites in place.

# Install Ulyssesreader

## Get the source code from GitHub



# Run ulyssesreader