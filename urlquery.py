import urllib
import BeautifulSoup

s1 = "https://urlquery.net/"

r = urllib.urlopen(s1)
soup = BeautifulSoup.BeautifulSoup(r.read())
[s.extract() for s in soup('img')]

for tr in soup.findAll('tr', {'class': 'odd_highlight'}):
    for td in tr:
        if td.center:
            print td.center.string
        if td.a:
            print td.a.get('title')
        if td.string:
            print td.string
    print " "

print soup.originalEncoding
