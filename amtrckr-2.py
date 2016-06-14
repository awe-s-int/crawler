import urllib
# import BeautifulSoup
from bs4 import BeautifulSoup

s1 = "http://amtrckr.info/"
soup = BeautifulSoup(urllib.urlopen(s1), 'lxml')
[s.extract() for s in soup('i')]
[s.extract() for s in soup('span')]

tables = soup.findAll('table')
my_table = tables[0]

rows = my_table.findAll(['th', 'tr'])

for row in rows:
    cells = row.findAll('td')
    if len(cells) > 5:
        print cells[0].string
        print cells[1].string
        print cells[2].a.string
        print cells[3].string
        print cells[4].a.get('href')
        print " "
