# Objective: Scrape the data from the website https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India
# Load the required libraries
import urllib2
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

# query the website and return the html of the page
page=urllib2.urlopen(url)
# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
# Take out the <div> of name and get its value

all_links= soup.find_all("a")
for link in all_links:
    print link.get("href")


all_tables=soup.find_all('table')
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
print right_table
#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

    # import pandas to convert list to data frame
import pandas as pd

df = pd.DataFrame(A, columns=['Number'])
df['State/UT'] = B
df['Admin_Capital'] = C
df['Legislative_Capital'] = D
df['Judiciary_Capital'] = E
df['Year_Capital'] = F
df['Former_Capital'] = G
df


# Load the library to write the data
import csv
from datetime import datetime
# open a csv file with append, so old data will not be erased
'''
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])

'''