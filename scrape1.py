from urllib2 import urlopen
from bs4 import BeautifulSoup as bs

html= urlopen("http://stackoverflow.com/?tab=hot")

htmlSO= urlopen("http://stackoverflow.com/?tab=featured")

bsObj = bs(html,"lxml")
bsObj1 = bs(htmlSO,"lxml")
nameList1= bsObj.find_all("a",{"class":"question-hyperlink"},recursive= True)
nameList2= bsObj1.find_all("div",{"class":"mini-counts"}, recursive= True)
# get all text enclosed in span attribute with class as green
# by setting recursive = true, will look into children and there children

for name in nameList1:
    print name.get_text() # .get_text() strips all tags from the document you are working with and returns a string containing the text only.

for count in nameList2:
    print count.get_text() # .get_text() strips all tags from the document you are working with and returns a string containing the text only.
# some more changes
