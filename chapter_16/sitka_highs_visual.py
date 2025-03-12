from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#extract the dates and high temps
dates, highs = [], []

for row in reader:
    high = int(row[4])
    highs.append(high)

# plotting the high temps
plt.style.use("fivethirtyeight")
fig, ax, = plt.subplots()
ax.plot(highs, color="red")

# formatting
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()