import pandas as pd
import matplotlib.pyplot as plt
import os

print('1')
stops = pd.concat([
    pd.read_csv(f"data/gtfs (2)/stops.txt"),
    pd.read_csv(f"data/gtfs (3)/stops.txt"),
    pd.read_csv(f"data/gtfs (4)/stops.txt")
])
print('1')
times = pd.concat([
    pd.read_csv(f"data/gtfs (2)/stop_times.txt"),
    pd.read_csv(f"data/gtfs (3)/stop_times.txt"),
    pd.read_csv(f"data/gtfs (4)/stop_times.txt")
])
print('1')
trip = pd.concat([
    pd.read_csv(f"data/gtfs (2)/trips.txt"),
    pd.read_csv(f"data/gtfs (3)/trips.txt"),
    pd.read_csv(f"data/gtfs (4)/trips.txt")
])
print('1')
out = pd.DataFrame()
out['id'] = stops.stop_id.unique()
print(type(out.id))
print(stops[stops.stop_id == 201].stop_name)
print(2)
out['name'] = out.apply(lambda row: stops[stops.stop_id == row.id].stop_name.iloc[0], axis=1)
print(3)

print(4)
out['lat'] = out.apply(lambda row: stops[stops.stop_id == row.id].stop_lat.iloc[0], axis=1)
print(5)
out['lon'] = out.apply(lambda row: stops[stops.stop_id == row.id].stop_lon.iloc[0], axis=1)
# print(6)
# out['wheelchair'] = out.apply(lambda row: trip[
#     trip.stop_id == row.stop_id
#     and trip.wheelchair_accessible == 1
# ].count() / trip[trip.stop_id == row.stop_id].count(), axis=1)

# out['bikes'] = out.apply(lambda row: trip[
#     trip.stop_id == row.stop_id
#     and trip.bikes_allowed == 1
# ].count() / trip[trip.stop_id == row.stop_id].count(), axis=1)

out['fequency'] = out.apply(
    lambda row: times[times.stop_id == row.id].trip_id.count(), axis=1)

print(out)
with open(f'data/old.csv', 'w+') as f:
    f.write(out.to_csv())
