import urllib
import urllib2
import ast

def enum(**enums):
    return type('Enum', (), enums)

def compareText(originText, compareText):
    """
    if the same, return 0  else return -1;
    Causion: if the last \n ignore
    
    """
    if originText.rstrip() == compareText:
        return 1
    else:
        return 0


def post(url, data):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)  
    return response.read()  

def parseJSON(data):
    return ast.literal_eval( data)
