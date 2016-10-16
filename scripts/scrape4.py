__author__ = 'ashish dutt'
from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL="https://scholar.google.com/citations?user=AIGfYdEAAAAJ&hl=en"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

