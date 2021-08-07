# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Adegbola.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')

#.get takes tag's attribute in this case, 'href'
lst = []
for tag in tags:
    lst.append(tag.get('href', None))
print(lst[17])

url = lst[17]
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

lst2 = []
for tag in tags:
    lst2.append(tag.get('href', None))
print(lst2[17])

url = lst2[17]
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

lst3 = []
for tag in tags:
    lst3.append(tag.get('href', None))
print(lst3[17])

url = lst3[17]
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

lst4 = []
for tag in tags:
    lst4.append(tag.get('href', None))
print(lst4[17])

url = lst4[17]
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

lst5 = []
for tag in tags:
    lst5.append(tag.get('href', None))
print(lst5[17])

url = lst5[17]
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

lst6 = []
for tag in tags:
    lst6.append(tag.get('href', None))
print(lst6[17])

url = lst6[17]
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

lst7 = []
for tag in tags:
    lst7.append(tag.get('href', None))
print(lst7[17])
