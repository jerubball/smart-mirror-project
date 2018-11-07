import requests
from bs4 import BeautifulSoup


def get_news():
    page = requests.get("https://www.nyit.edu/box")
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find_all('p', class_='serif-italic-medium')
    date = soup.find_all('p', class_='monospace-regular-xsmall')
    news = dict()
    news["title"] = title
    news["date"] = date
    result = list()
    for title, date in zip(news["title"], news["date"]):
        newsitem = dict()
        newsitem["title"] = title.find('a').text
        type_and_date = str(date.text).split(' | ')
        if len(type_and_date) > 0:
            newsitem["type"] = type_and_date[0]
        else:
            newsitem["type"] = ""
        if len(type_and_date) > 1:
            newsitem["date"] = type_and_date[1]
        else:
            newsitem["date"] = ""
        result.append(newsitem)
    return result
