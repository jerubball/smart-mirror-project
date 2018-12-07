import requests
import pandas as pd
import time


stations_url = 'http://mtaapi.herokuapp.com/api?id=125S'

response = requests.get(stations_url)

station_name = response.json()['result']['name']
station_arrivals = response.json()['result']['arrivals']

df = pd.read_json(stations_url)

arrivals = df['result']['arrivals']


def trains(hour, minute, second):
    trains_url = "http://mtaapi.herokuapp.com/times?hour=" + hour + "&minute=" + minute
    r = requests.get(trains_url)
    rr = r.json()
    result = []

    for train in rr['result']:
        if train['name'] == "59 St - Columbus Circle" and train['arrival'] == hour+':'+minute+':'+second:
            current_train = train['id']
            result.append(current_train[0])
    return result


def arriving_trains(local=None, within=1):
    current_time = time.localtime(local)
    future_time = time.localtime(time.mktime(current_time) + within * 3600)
    print("LOCAL TIME: " + time.strftime("%H:%M:%S", current_time))
    print("FUTURE TIME: " + time.strftime("%H:%M:%S", future_time) + "\n")
    result = list()

    for arrive in arrivals:
        arr = arrive.split(':')
        arrive_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, int(arr[0] == "24" and "0" or arr[0]), int(arr[1]), int(arr[2]), current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))
        if current_time < arrive_time < future_time:
            times = time.strftime("%H:%M:%S", arrive_time)
            train_names = str(trains(arr[0], arr[1], arr[2]))
            train_data = dict()
            train_data["train_times"] = times
            train_data["train_names"] = train_names
            result.append(train_data)
    return result
