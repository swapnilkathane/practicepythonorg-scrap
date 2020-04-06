import requests
from bs4 import BeautifulSoup
pp=requests.get('https://www.practicepython.org/')
soup=BeautifulSoup(pp.text, 'html.parser')
code=soup.prettify()
a=soup.title.text
print("Title of website is : ",a)
print(' ')
b=soup.div.h2.text
print("Tagline of website is : ",b)
print(' ')
c=soup.find('ul')
d=c.find_all('li')
print('Header tabs in practice python wedsite are : ')
for i in d:
    print(i.a.text)

e=soup.find('div', class_="left")
f=e.find('h2',class_='midheader')
print(' ')
print(f.text)
print(" ")
g=e.find('ul')
h=g.find_all('li')
l=1
for o in h:
    print(l,o.a.text)
    l+=1







