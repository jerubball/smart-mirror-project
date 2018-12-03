import requests
import pandas as pd

local = "04:01:52 PM"
stations_url = 'http://mtaapi.herokuapp.com/api?id=125S'

response = requests.get(stations_url)

station_name = response.json()['result']['name']
station_arrivals = response.json()['result']['arrivals']

df = pd.read_json(stations_url)

arrivals = df['result']['arrivals']
# newlist = []
# locals = []
# local = local.split(";")

# for time in arrivals:
#     times = time.split(":")
#     newlist.append(int(times[0])*3600+int(times[1])*60+int(times[2]))
#     print(newlist)

print("\n" + station_name + "\n")


def arriving_trains(local_time):
    within = 2
    added_hour = int(local_time[0:2]) + within

    # Catch hour(s) over 24 hours
    # ==============> (1) <==============
    if 24 < added_hour:
        added_hour = "0" + str(within)

    print("LOCAL TIME: " + local_time[0:8])
    if local_time[0] == "0":
        future_time = (local_time[0] + str(added_hour) + local_time[2:8])
    elif local_time[0:2] == "00":
        future_time = (local_time[0:2] + str(added_hour) + local_time[2:8])
    else:
        future_time = (str(added_hour) + local_time[2:8])

    print("FUTURE TIME: " + future_time + "\n")

    # Display range of times
    # ==============> (3) <==============
    for time in arrivals:
        if local_time < time > future_time:
            print(time)


arriving_trains(local)

# TODO:
# Implement if statement (1) to catch added hour(s) that go over 24
# Fix if statement (3) to display the correct range of times from local and future time
