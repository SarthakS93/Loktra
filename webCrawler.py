import requests
from bs4 import BeautifulSoup
import sys
import re

url1 = "http://www.shopping.com/products?KW="
url2 = "http://www.shopping.com/products~PG-"

def query1():
    url = url1 + sys.argv[1]
    r = requests.get(url)
    if r.status_code != 200:
        print("Exception")
        return
    else:
        soup = BeautifulSoup(r.text)
        temp = soup.find(class_ = 'numTotalResults')
        if temp == None:
            print('No Results')
        else:
            slicedList = temp.text.split(' ')
            if len(slicedList) == 0:
                print('No Results')
            else:
                result = slicedList[-1]
                result = result[:-1]
                print('The number of reults for ' + sys.argv[1]
                        + ' are:', result)


def query2():
    url = url2 + sys.argv[1] + '?KW=' + sys.argv[2]
    r = requests.get(url)
    if r.status_code != 200:
        print("Exception")
        return
    else:
        soup = BeautifulSoup(r.text)
        results = soup.find_all(text = re.compile(sys.argv[2]))
        if len(results) == 0:
            print("No results found")
        else:
            links = soup.find_all('a', text = re.compile(sys.argv[2]))

            print('The brute force search results are as follows:')
            for l in results:
                print(l)
            print('The number of brute force search results is:',
                    len(results))
            if len(links) == 0:
                return
            else:
                print('The number of links:', len(links))
                print('The links results are as follows:')
                for l in links:
                    print('LINK: ' + l['href'] + ' TEXT: ' + l.string)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter valid arguments')
    else:
        if len(sys.argv) == 2:
            query1()
        else:
            query2()
