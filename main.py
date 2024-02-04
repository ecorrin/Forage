from pyscript import display
import folium
import json
import pandas as pd

from pyodide.http import open_url

url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
state_geo = f"{url}/us-states.json"
state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
state_data = pd.read_csv(open_url(state_unemployment))
geo_json = json.loads(open_url(state_geo).read())

m = folium.Map(location=[51.55, -0.0500], zoom_start=17)



# Creating data set for Latitude, Longitude
geolocations = [
("51.53914", "-0.03511"),
("51.53853", "-0.03616")
]
# data set created

# marker creation - running through data set one by one to produce equivalent set of markers. The marker function seems to take coordinates as its parameters, cords.
for cords in geolocations:
    folium.Marker(location=[cords[0], cords[1]]).add_to(m)
# end of marker creation

# create new list of plant names that match the geolocations
plant_names = [

    "Wild chives",
    "Magpie mushroom"
]
# end of list

# add display info – note, for testing leave in the Lat and Long pop up display but strip out in final version
for cords, name in zip(geolocations, plant_names):
    folium.Marker(location=[cords[0], cords[1]],
                  popup=f"Latitude:<br>{cords[0]}<br>"
                        f"Longitude:<br>{cords[1]}<br>"
                        f"Name:<br>{name}"
                  ).add_to(m)
# end display code

# fit bounds function automatic zoom in
south_west_corner = min(geolocations)
north_east_corner = max(geolocations)
my_map_name.fit_bounds([south_west_corner, north_east_corner])
# end fit bounds code

# save and run
m.save("my_map_visual.html")
m



display(m, target="folium")
