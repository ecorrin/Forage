
import folium
import folium.plugins as plugins

m = folium.Map([41.97, 2.81])

folium.plugins.LocateControl().add_to(m)
m
