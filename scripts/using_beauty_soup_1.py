__author__ = 'ashish dutt'
# Learning Beautiful Soup
# Beautiful Soup includes the following objects viz: BeautifulSoup, tag, Navigable String.
# This example is focussed on object BeautifulSoup.
# Step 1: import beautifulsoup and urllib2 library. The urllib2 library will open the connection to webpage and beautifulsoup will create the required object
from bs4 import BeautifulSoup
import urllib2
# Step 2: Create the beautiful soup object
url="http://stackoverflow.com/questions/4328271/best-way-for-a-beginner-to-learn-screen-scraping-by-python"
url1="http://stackoverflow.com/?tab=featured"
page=urllib2.urlopen(url)
page1=urllib2.urlopen(url1)

#Step 2.1: To create the html object use the features argument in BeautifulSoup object as html. See below example
soup_page_html=BeautifulSoup(page, features="html")
print soup_page_html
#Step 2.2: To create the xml object use the features argument in BeautifulSoup object as xml. See below example
soup_page_xml=BeautifulSoup(page, features="xml")
soup_page_lxml=BeautifulSoup(page1, features="lxml")
#print soup_page_xml
# Note: The features argument helps us to choose between HTML/XML parsing for the document.
# Note: lxml is used for xml object. Therefore lxml must be installed on the system to work. if not then you get error
# Note: it is good to specify the parser by giving the features argument because this helps to ensure that the input is processed in the same manner across different machines. Otherwise, there is a possibility that the same code will break in one of the machines if some invalid HTML is present, as the default parser that is picked up by Beautiful Soup will produce a different tree. Specifying the features argument helps to ensure that the tree generated is identical across all machines.

# The Tag object represents different tags of HTML and XML documents.
# The Tag objects can be used for searching and navigation within the HTML/XML document.
# Step 3: Accessing the Tag object
tag=soup_page_html.a
print "### Will print the first <a> tag in the document. ###\n"
print tag
tag=soup_page_html
print "### Print the attribute of the tag ###\n"
print tag.attrs

# Step 3.1: To get a list of all attributes associated to an object use the .attrs property as given
print "### Print the attributes associated to the tag ###\n"
print tag.attrs
# A NavigableString object holds the text within an HTML or an XML tag.
#  Sometimes we may need to navigate to other tags or text within an HTML/XML document based on the current text.
# We can get the text stored inside a particular tag by using ".string".
print "### Print the text stored inside the tag ###\n"
print tag.string

# Step 4: Search using Beautiful Soup
# Beautiful Soup comes with inbuilt search methods listed as follows: find(), find_all(), find_parent(),find_parents(),find_next_sibling(),find_next_siblings(),find_previous_sibling(),find_previous_siblings()

## Example 1: Find tags
tags_a=soup_page_html.find("li")
print "\n### Print <li> tag in the page ###"
print tags_a
tags_a=soup_page_html.find("div", {"class":"post-text"})
print "\n### Print the first comment in the page ###"
print tags_a

tags_a=soup_page_html.find_all("div", {"class":"post-text"},recursive= True)
print "\n### Print the all comments in the page ###"
print tags_a

tag_user_score=soup_page_lxml.find_all("span",{"class":"reputation-score"},recursive= True)
print "\n### Print user reputation score ###"
print tag_user_score # will print the content with html tags
print "\n"
