import csv
import pandas as pd

rows = []

with open("Pro-134(f).csv","r") as f :
  csvR = csv.reader(f)
  for row in csvR :
    rows.append(row)

header = rows[0]
planetData = rows[1:]
print(planetData)

header[0] = "Index"

data = []
for planet_data in planetData :
  print(planet_data[1])
  # temp_dict = {
  #     "name" : planet_data[1],
  #     "distance" : planet_data[2],
  #     "mass" : planet_data[3],
  #     "radius" : planet_data[4],
  #     "gravity" : planet_data[5]
  # }
  # data.append(temp_dict)
