import requests
import json
import math
best_match = 0
response = requests.get("https://geoweb1.digistadtdo.de/doris_gdi/geoserver/parken/ogc/features/collections/pls/items?f=application%2Fgeo%2Bjson")
res = json.loads(response.text)
user_x_cord = float(input("Was ist deine x Koordinate? "))
user_y_cord = float(input("Was ist deine y Koordinate? "))
x_cord = float(res["features"][0]["geometry"]["coordinates"][0])
y_cord = float(res["features"][0]["geometry"]["coordinates"][1])
distance = math.sqrt((user_x_cord - x_cord)**2 + (user_y_cord - y_cord)**2)
for i in range(1,len(res["features"])):
    x_cord2 = float(res["features"][i]["geometry"]["coordinates"][0])
    y_cord2 = float(res["features"][i]["geometry"]["coordinates"][1])
    new_distance = math.sqrt((user_x_cord - x_cord2)**2 + (user_y_cord - y_cord2)**2)
    if new_distance < distance:
        distance = new_distance
        best_match = i
print(res["features"][best_match]["properties"]["name"])

