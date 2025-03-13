from pathlib import Path
import csv
import matplotlib.pyplot as plt


path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

#for index, columb_header in enumerate(header_row):
#   print(index, columb_header)

highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

