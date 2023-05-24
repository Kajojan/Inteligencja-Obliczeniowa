# import cartopy.crs as ccrs
# import matplotlib.pyplot as plt
# from geopy.geocoders import Nominatim
# import json
# import time
# geolocator = Nominatim(user_agent="my-")

# location=[]

# # Tworzenie obiektu geokodera

# # Przykładowa lokalizacja tweeta
# tweet_location = "London, UK"

# # Geokodowanie lokalizacji tweeta

# # Tworzenie mapy
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())

# # Ustawienie obszaru mapy
# ax.set_extent([-10, 30, 35, 60], crs=ccrs.PlateCarree())
# ax.set_global()
# # Dodanie tła mapy
# ax.stock_img()
# i=0
# # Dodanie lokalizacji tweeta na mapę
# with open("./data/twitter23.jsonl", 'r') as file:
#     for line in file:
#         if(i <= 10): 
#             i+=1
#             parsed_data = json.loads(line)
#             loc = parsed_data['user']['location']
#             location = geolocator.geocode(loc)
#             time.sleep(1)
#             if(location != None):
#                 ax.plot(location.longitude, location.latitude, 'ro',markersize=1 , transform=ccrs.PlateCarree())
#         else:
#             break
# # Dodanie siatki z podziałką geograficzną
# ax.gridlines()

# # Wyświetlenie mapy
# plt.show()


import matplotlib.pyplot as plt
import seaborn as sns
import json
from geopy.geocoders import Nominatim
import time
import cartopy.crs as ccrs

geolocator = Nominatim(user_agent="my")

# Przygotowanie danych - przykładowe punkty (długość, szerokość geograficzna)
points = [
    (-0.127758, 51.507351),  # Londyn
    (2.352222, 48.856614),   # Paryż
    (13.404954, 52.520008),  # Berlin
    (-73.935242, 40.730610), # Nowy Jork
    (139.691706, 35.689487), # Tokio
    # Dodaj więcej punktów...
]
fig = plt.figure(figsize=(10, 8))

ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())

i=0
with open("./data/twitter23.jsonl", 'r') as file:
    for line in file:
        if(i <= 10): 
            i+=1
            parsed_data = json.loads(line)
            loc = parsed_data['user']['location']
            location = geolocator.geocode(loc)
            time.sleep(1)
            if(location != None):
                ax.plot(location.longitude, location.latitude, 'ro',markersize=1 , transform=ccrs.PlateCarree())
        else:
            break

# Przygotowanie danych do heatmapy
lon = [point[0] for point in points]
lat = [point[1] for point in points]

# Tworzenie heatmapy
fig, ax = plt.subplots(figsize=(10, 8))
sns.kdeplot(lon, lat, cmap='hot', shade=True, ax=ax)

# Ustawienia mapy
ax.set_xlim(min(lon), max(lon))
ax.set_ylim(min(lat), max(lat))
ax.set_xlabel('Długość geograficzna')
ax.set_ylabel('Szerokość geograficzna')
ax.set_title('Heatmapa punktów')

# Wyświetlenie heatmapy
plt.show()
