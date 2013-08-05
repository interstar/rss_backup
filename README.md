RSS Backup
==========

This is an update of QuoraGrabber. A short script to grab items from rss-feeds and back them up on local machine.

I'm using it so I can ensure I have a local copy of all the writing I'm putting into say my Blogspot blogs.

QuickStart
----------

Make sure you have Python installed. 

You'll need a couple libraries that can be installed using easy_install.

    easy_install feedparser
    easy_install beautifulsoup4
    

Now ...

    git clone https://github.com/interstar/rss_backup.git rss
    cd rss
    git submodule update --init
    python grab_rss.py http://feeds.theguardian.com/theguardian/uk/rss Guardian
    python list.py "The Guardian" > g.html
    firefox g.html
    

What did I just do?
-------------------

You 

1. pulled down a feed of recent stories from The Guardian via its RSS feed
2. stored each in a separate file
3. produced a quick HTML page (g.html) to display them.

(The Guardian here is just used as an example. You'll probably have a feed of your own you want to grab.)


Why?
----

I wrote this script to ensure that I could easily back-up the writing I'm doing on social media sites like 
Quora and on my blogs hosted on Blogspot. I don't like the idea that most of my writing only exists in 
someone else's silo. I, at least, want to have a copy of it on my local machine. In future I may write 
other scripts to do something more useful with it.


I Only Came Here Because You Said Something About Quora
-------------------------------------------------------

OK. There's a special script to make that easier.

    python grab_quora.py YOUR-QUORA-USER-NAME
    python list.py "A TITLE" > quora.html
    firefox quora.html



FAQ
---
Q : Why do the files have such weird names?

A : The file names are based on the titles of posts but they needed to be both a) shorter than the original titles, and b) unique.

A "hashing" function takes a piece of text and is *almost* certain to come up with a unique code-number based on it, so 
I'm using a hashing function to generate a filename from the title which is short(ish), but almost certainly unique.

Q : I looked inside the file and its weird.

A : I'm storing answers in JSON format. A very simple data-structure that most pramming languages can handle very 
easily. (More easily than XML in most cases.) 

This gives other people the chance to write scripts to render those answers in different human readable formats. The 
list.py program included here puts them into a single HTML page. But there'll be other options. Talk to me if you'd 
like to request one.




