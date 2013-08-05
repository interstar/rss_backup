from grab_rss import *

if __name__ == '__main__' :
    from sys import argv
    name = argv[1]
    url = "http://www.quora.com/%s/answers/rss" % name
    grab(url,name)

