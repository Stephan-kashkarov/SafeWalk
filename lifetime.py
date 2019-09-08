import pandas as pd
import matplotlib.pyplot as plt
import requests

def coordToSuburb(lat, lon):
    return requests.get(
        'https://reverse.geocoder.api.here.com/6.2/reversegeocode.json',
        data={
            'prox': f"{lat},{lon}",
            'mode': 'retrieveAddresses',
            'maxresults': '1',
            'gen': '9',
            'app_id': 'devportal-demo-20180625',
            'app_code': '9v2BkviRwi9Ot26kp2IysQ'
        }
    ).json()['View']['Result']['Address']['District']

pop = pd.read_csv('data/ACT_Population_Projections_by_Suburb__2015_-_2020_.csv')

pop['total'] = pop.apply(
    lambda row: sum([row[x] for x in pop.columns[2:]]),
    axis=1
)

pop = pop.drop(columns=[x.strip() for x in pop.columns[2:-1]])

pop['Suburb'] = pop['Suburb'].str.strip()
print(pop.Suburb.unique())

print(pop.head())


# for sub in pop.Suburb.unique():
#     pop[pop.Suburb == sub].plot()
#     plt.show()

def gen_year_bus(file):
    temp = pd.DataFrame()
    stop = pd.read_csv(f"{file}/stops.txt")
    stop_times = pd.read_csv(f"{file}/stop_times.txt")

    temp['id'] = stop.stop_id.unique()
    temp['freq'] = temp.apply(
        lambda row: stop_times[stop_times.stop_id == row.id].trip_id.count(), axis=1
    )

    temp['Suburb'] = temp.apply(
        lambda row: coordToSuburb(
            stop[stop.stop_id == row.id].lat,
            stop[stop.stop_id == row.id].lon
        )
    )


    
