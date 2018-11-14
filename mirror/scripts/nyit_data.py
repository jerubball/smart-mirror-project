import requests
from bs4 import BeautifulSoup


def get_events():
    page = requests.get("https://www.nyit.edu/events")
    soup = BeautifulSoup(page.content, 'html.parser')
    event_data = soup.find_all('a', class_='degree-block event-block')
    event = dict()
    event["title"] = event_data
    event["date"] = event_data
    event["location_and_time"] = event_data
    result = list()
    for event_title, event_date, event_location_and_time in zip(event["title"], event["date"], event["location_and_time"]):
        eventitem = dict()
        eventitem["title"] = event_title.find('h2').text
        eventitem["date"] = event_date.find('strong').text
        location_and_time = event_location_and_time.find_all('p', class_='monospace-regular-xsmall')
        if len(location_and_time) > 0:
            eventitem["location"] = location_and_time[0].text
        else:
            eventitem["location"] = ""
        if len(location_and_time) > 1:
            eventitem["time"] = location_and_time[1].text
        else:
            eventitem["time"] = ""
        result.append(eventitem)
    return result


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
