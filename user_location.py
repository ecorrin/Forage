from pyscript import display
import folium
import json
import pandas as pd
import folium.plugins as plugins

from pyodide.http import open_url



m = folium.Map([41.97, 2.81])

folium.plugins.LocateControl().add_to(m)


m
