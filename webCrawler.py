import requests
from bs4 import BeautifulSoup
import sys

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
                print('The number of reults are: ', result)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter valid arguments')
    else:
        if len(sys.argv) == 2:
            query1()
        else:
            query2()
