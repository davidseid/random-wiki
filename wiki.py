#!/usr/bin/env python
# -*- coding: utf-8 -*-


# PROJECT Random Wikipedia Article

'''
Background
If you've been to Wikipedia, you may have noticed that there is a link to a random article 
on the left side of the screen. While it can be fun to see what article you get taken to, 
sometimes it would be nice to see the name of the article so you can skip it if it sounds 
boring. Luckily, Wikipedia has an API that allows us to do so (Click here).

However, there is a dilemma. Since Wikipedia has articles about topics from all over the 
world, some of them have special characters in the title. For example, the article about 
the spanish painter Erasto Cortés Juárez has é and á in it. If you look at this specific 
article's API, you will see that the title is "Erasto Cort\u00e9s Ju\u00e1rez" and that 
the \u00e9 and \u00e1 are replacing the two previously mentioned letters. (For information 
about what this is, start by checking out the first half of this page in the documentation). 
To make your program work, you're going to have to handle this problem somehow.


Goal
Create a program that pulls titles from the official Wikipedia API and then asks the user 
one by one if he or she would like to read about that article. So if the first title is 
Reddit, then the program should ask something along the lines of "Would you like to read 
about Reddit?" If the user says yes, then the program should open up the article for the 
user to read.

HINT: Mouse over the hidden area below to see how the article's ID can be used to access 
the actual article. http://en.wikipedia.org/wiki?curid=39608394


Subgoals
As mentioned before, do something about the possibility of unicode appearing in the title. 
Whether you want your program to simply filter out these articles or you want to actually 
turn the codes into readable characters, that's up to you.
Make the program pause once the user has selected an article to read, and allow him or her 
to continue browsing different article titles once finished reading.

Allow the user to simply press ENTER to be asked about a new article.
'''

# author: David Seidenberg

# imports
import json
import urllib2
import time
import webbrowser

# Program Intro Message
intro = '''
Hello, welcome to my Random Wikipedia Article app, which interacts with Wikipedia's API in 
in order to offer random (and hopefully interesting) wikipedia articles for you to read if
you choose to read if you like.
'''
print intro


# pull titles from official Wikipedia API
url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json'


# loop to offer new articles
while True:

	article_no = 1

	data = json.load(urllib2.urlopen(url))

	while article_no <= 9:
		title = data['query']['random'][article_no]['title']
		
		proceed = raw_input("\n\nPress ENTER to be offered a new article to read.")
		
		print "\n\n\nWould you like to read about %s?"  %  title

		read = raw_input("\n\nType yes or no\n\n>>")

		id = str(data['query']['random'][article_no]['id'])

		article = "http://en.wikipedia.org/wiki?curid=" + id

		if read == "yes":
		
			print "\n\nGreat. Opening the article for you."
			print "When you are done, come back and we will offer more."
			time.sleep(2)
			webbrowser.open(article)
			time.sleep(5)
			article_no += 1
			
		elif read == "no":
			article_no += 1
			
		else:
			print "\n\nI'm sorry, I didn't understand."
			
