RSS Backup
==========

This is an update of QuoraGrabber. A short script to grab items from rss-feeds and back them up on local machine.

I'm using it so I can ensure I have a local copy of all the writing I'm putting into say my Blogspot blogs.

QuickStart
----------

Make sure you have Python installed.

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

I wrote this script to ensure that I could easily back-up the writing I'm doing on social media sites like Quora and on my blogs hosted on Blogspot. I don't like the idea that most of my writing only exists in someone else's silo. I, at least, want to have a copy of it on my local machine. In future I may write other scripts to do something more useful with it.



