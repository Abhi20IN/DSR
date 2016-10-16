import urllib2
from bs4 import BeautifulSoup

# Scraping craigslist
# 1. create the webpage handle
url="https://malaysia.craigslist.org/search/sss"
page= urllib2.urlopen(url)
# 2. Create the Beautiful Soup object
soup_page_html= BeautifulSoup(page,"lxml")
# 3. access the tag
tag_result= soup_page_html.findAll("span",{"class":"price"})
for price in tag_result:
    print price
    print "\n"

# ToDo activity: Find out how to strip the tag from tag_result



page.close() # Be nice, close the connection