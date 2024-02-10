import folium
import folium.plugins as plugins

m = folium.Map()

folium.plugins.LocateControl().add_to(m)
m
