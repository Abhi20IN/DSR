' This scripts uses beautiful soup for scraping'
'Simple program'
from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup as bs

try:
    html= urlopen("http://genomicsclass.github.io/book/pages/dplyr_tutorial.html")
except HTTPError as e:
    print e

bsObj= bs(html.read(),"lxml")
print bsObj.find_all("p")

