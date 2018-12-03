import requests
import pandas as pd

local = "24:00:00 PM"  # Change me to test some values
time_travel = 10       # Change me too

stations_url = 'http://mtaapi.herokuapp.com/api?id=125S'

response = requests.get(stations_url)

station_name = response.json()['result']['name']
station_arrivals = response.json()['result']['arrivals']

df = pd.read_json(stations_url)

arrivals = df['result']['arrivals']
print("\n" + station_name + "\n")


def arriving_trains(local_time, within):
    print("LOCAL TIME: " + local_time)

    new_hour = int(local_time[0:2]) + within
    new_day = False
    carry_over = 0

    # Catch hour(s) over 24 hours
    if new_hour > 24:
        new_day = True
        carry_over = new_hour - 24

    if new_day and carry_over >= 10:
        future_time = (str(carry_over) + local_time[2:8])
    elif new_day:
        future_time = ("0" + str(carry_over) + local_time[2:8])
    elif local_time[0] == "0":
        future_time = (local_time[0] + str(new_hour) + local_time[2:8])
    else:
        future_time = (str(new_hour) + local_time[2:8])

    if int(future_time[0:2]) < 10:
        print("FUTURE TIME: " + future_time + " AM\n")
    else:
        print("FUTURE TIME: " + future_time + " PM\n")

    # Display range of times
    # ==============> (3) <==============
    for time in arrivals:
        if carry_over > int(time[0:2]) < new_hour:
            print(time)


arriving_trains(local, time_travel)


# -------------------------------------------------------------------------

# TODO:
# Fix if statement (3) to display the correct range of times from local and future time

# -------------------------------------------------------------------------

# Scraps:
# newlist = []
# locals = []
# local = local.split(";")

# for time in arrivals:
#     times = time.split(":")
#     newlist.append(int(times[0])*3600+int(times[1])*60+int(times[2]))
#     print(newlist)

# -------------------------------------------------------------------------

# if local_time[0] == "0":
#     future_time = (local_time[0] + str(added_hour) + local_time[2:8])
#     print("1")
# elif local_time[0:2] == "00":
#     future_time = (local_time[0:2] + str(added_hour) + local_time[2:8])
#     print("2")
# else:
#     future_time = (str(carry_over) + local_time[2:8])
#     print("3")
