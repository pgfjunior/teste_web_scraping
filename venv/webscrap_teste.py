import urllib.request

from bs4 import BeautifulSoup

page = urllib.request.urlopen('https://www.dentalcremer.com.br/')

soup = BeautifulSoup(page, "html.parser")

print(soup.find_all('table'))
