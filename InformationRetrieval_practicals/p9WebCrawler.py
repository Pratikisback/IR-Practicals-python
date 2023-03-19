import requests
from bs4 import BeautifulSoup
url = ("www.google.com")
code = requests.get("http://"+url)
plain = code.text
s= BeautifulSoup(plain, "html.parser")
for link in s.find_all('a'):
    href = link.get('href')
    print(href)