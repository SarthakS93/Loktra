# get the scheme of a url
def getScheme(u):
    url = u.lower()
    temp = url.split('/')
    if len(temp) < 3:
        print('Incorrect URL')
    else:
        scheme = temp[0].split(':')[0]
        if scheme != 'http' and scheme != 'https':
            print('Incorrect URL')
        else:
            return scheme


# helper function to replace space btw words with '+'
def formatString(v):
    if type(v) is str:
        temp = v.split(' ')
        s = ''
        for t in temp:
            s += t
            return s[:-1]
    else:
            return str(v)

# urlencode
def encodeUrl(q):
    if type(q) is dict:
        s = ''
        for k, v in q.items():
            s += k + '='
            s += formatString(v) + '&'
        return s[:-1]
    else:
        print('Argument not a dictionary')
