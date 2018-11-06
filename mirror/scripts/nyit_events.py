import requests
from bs4 import BeautifulSoup


def get_events():
    page = requests.get("https://www.nyit.edu/events")
    soup = BeautifulSoup(page.content, 'html.parser')
    event_title = soup.find_all('a', class_='degree-block event-block')
    event_date = soup.find_all('a', class_='degree-block event-block')
    event_location_and_time = soup.find_all('a', class_='degree-block event-block')
    event = dict()
    event["title"] = event_title
    event["date"] = event_date
    event["location_and_time"] = event_location_and_time
    result = list()
    for event_title, event_date, event_location_and_time in zip(event["title"], event["date"], event["location_and_time"]):
        #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        '''
        print(event_title.find('h2').text)
        print(event_date.find('strong').text)
        location_and_time = event_location_and_time.find_all('p', class_='monospace-regular-xsmall')
        for item in location_and_time:
            print(item.text)
        '''
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
        #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return result
