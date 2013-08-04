from os import listdir
from os.path import isfile, join
import cgi

onlyfiles = [ f for f in listdir(".") if isfile(join("",f)) ]

import json
from sys import argv

def u2h(text):
    """Converts unicode to HTML entities.  For example '&' becomes '&amp;'."""
    text = cgi.escape(text).encode('ascii', 'xmlcharrefreplace')
    return text

print """
<html>
<style>
body {
    font-family:sans;
    color:#333333;
    padding:3px;
}

dt {
    top-margin:4px;
    font-weight:bold;
}


</style>
<body>
<h2>%s</h2>
<dl>
""" % argv[1]

count = 0
for fn in onlyfiles :
    if fn[-3:] == "txt":
        f = open(fn) 
        entry = json.loads(f.read())
        
        print "<dt>%s <a href='%s'>Link</a></dt>" % (entry["question"].encode('ascii', 'xmlcharrefreplace'), entry["link"].encode('ascii', 'xmlcharrefreplace'))
        
        answer = entry["answer"].encode('ascii', 'xmlcharrefreplace')
        #answer = u2h(answer)
        answer = answer.replace("\n\n","<br/>")
        print "<dd>%s</dd>" % answer
        print "<hr/>"
        count = count+1
        
print """
</dl>
<p>%s items</p>
</body>
</html>""" % count
