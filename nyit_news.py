import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.nyit.edu/box")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find_all('p', class_='serif-italic-medium')
date = soup.find_all('p', class_='monospace-regular-xsmall')

news = dict()
news["title"] = title
news["date"] = date
for title, date in zip(news["title"], news["date"]):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(title.find('a').text)
    print(date.text)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
