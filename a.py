import csv
import pandas as pd 
 

rows = []

with open("main.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

df = pd.read_csv("main.csv")




low_dist_stars = list(df)
for df in low_dist_stars:
  if df[float(2)] < 150 or df[int(2)] > 350:
    low_dist_stars.remove(df)

print(len(low_dist_stars))

df.to("final.csv")



