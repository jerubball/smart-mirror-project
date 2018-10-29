import requests
from bs4 import BeautifulSoup


def get_events():
    page = requests.get("https://www.nyit.edu/events")
    soup = BeautifulSoup(page.content, 'html.parser')
    event_title = soup.find_all('a', class_='degree-block event-block')
    event_date = soup.find_all('a', class_='degree-block event-block')
    event_location = soup.find_all('a', class_='degree-block event-block')
    event_time = soup.find_all('a', class_='degree-block event-block')
    event = dict()
    event["title"] = event_title
    event["date"] = event_date
    event["location"] = event_location
    for event_title, event_date, event_location in zip(event["title"], event["date"], event["location"]):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(event_title.find('h2').text)
        print(event_date.find('strong').text)
        location_and_time = event_location.find_all('p', class_='monospace-regular-xsmall')
        for item in location_and_time:
            print(item.text)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
