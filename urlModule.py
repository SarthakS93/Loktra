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
            s += t + '+'
        return s[:-1]
    else:
        return str(v)

# urlencode
def encodeUrl(q):
    if type(q) is dict:
        s = ''
        for k, v in q.items():
            s += k + '='
            s += formatString(v)
            s += '&'
        return s[:-1]
    else:
        print('Argument not a dictionary')

# get domain
def getDomain(u):
    url = u.lower()
    main = {'com':True,'co':True,'in':True,'org':True,'edu':True,
            'net':True,'int':True,'gov':True,'mil':True}
    sec = {'uk':True,'us':True,'in':True,'de':True,'au':True,
            'fr':True,'it':True,'es':True}
    temp = url.split('.')
    if temp[-1] in main or temp[-1] in sec:
        return temp[-1]
    else:
        return 'Sorry, URL cant be processed'
