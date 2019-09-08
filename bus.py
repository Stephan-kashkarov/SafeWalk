import pandas as pd
import matplotlib.pyplot as plt
import os

stops = pd.concat([
    pd.read_csv(f"data/gtfs (0)/stops.txt"),
    pd.read_csv(f"data/gtfs (1)/stops.txt")
])
times = pd.concat([
    pd.read_csv(f"data/gtfs (0)/stop_time.txt"),
    pd.read_csv(f"data/gtfs (1)/stop_time.txt")
])
out = pd.DataFrame()
out['id'] = stops.stop_id.unique()
out['name'] = stops[stops.stop_id == out.id].stop_name
out['usage'] = times[times.stop_id == out.id].count()
out['lat'] = stops[stops.stop_id == out.id].stop_lat
out['long'] = stops[stops.stop_id == out.id].stop_long


with open(f'data/new.csv') as f:
    pass
