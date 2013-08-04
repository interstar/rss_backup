import feedparser
import hashlib
import json
from bs4 import BeautifulSoup, Tag

from html import html

def flatten(tag,keeplist) :
    if not isinstance(tag,Tag) : return tag
    
    children = []
    for t in tag.contents :
        children.append(flatten(t,keeplist))
            
    if tag.name in keeplist :
        return html.tag(tag.name,tag.attrs,"".join(children))
        
    return "".join(children)
    
def grab(url,ext) :
    d = feedparser.parse(url)
    for e in d["entries"] :
        title = e["title"].encode("utf-8")
        summary = e["summary"]
        h = hashlib.sha224(title).hexdigest()
        summary = summary.replace("<br />","__LINEBREAK__")  
          
        soup = BeautifulSoup(summary)
        
        s = flatten(soup.contents[0],["a","b","code","pre","i","blockquote", "img","iframe"])

        answer = s.encode("utf-8")
        answer = answer.replace("__LINEBREAK__","\n")
        answer = answer.strip()
        print "TITLE " +  title
        print "ANSWER <<<%s>>>" % answer
        j = {"question":title,"answer":answer,"link":e["link"]}
        f=open(h+".%s.txt"%ext,'w')
        f.write(json.dumps(j))
        
        f.close()
 

if __name__ == '__main__' :
    from sys import argv
    print argv
    grab(argv[1],argv[2])
    
