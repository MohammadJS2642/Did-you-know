from os import device_encoding
from bs4 import BeautifulSoup
import requests
import json
import io

url = 'https://fa.wikipedia.org/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C'
req = requests.get(url).content
soup = BeautifulSoup(req, 'html.parser')

first_div = soup.find_all('div', attrs={'class': 'mw-parser-output'})
second_div = soup.find_all('div', attrs={'id': 'mp-left'})
thirth_div = soup.find_all('div', attrs={'id': 'mf-fp'})

for div in first_div:
    Selected_article = div.find('div', {'id': 'mf-fa'})
    did_you_know = div.find_all('div', {'id': 'mf-con'})

for inDiv in did_you_know:
    t = inDiv.find_all('div', {'style': 'padding: 0 0.5em;'})
    for nextDiv in t:
        ul = nextDiv.find_all('ul')
        for lst in ul:
            li = lst.text

for div in second_div:
    Monuments = div.find('div', {'id': 'mf-otd'})

for div in thirth_div:
    Selected_image_today = div.find('div', {'class': 'center'})

print(li)