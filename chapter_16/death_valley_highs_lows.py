from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#extract the dates, low and high temps
dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"No data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# plotting the high temps
plt.style.use("fivethirtyeight")
fig, ax, = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5, lw=1)
ax.plot(dates, lows, color="blue", alpha=0.5, lw=1)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# formatting
ax.set_title("Daily High and Low Temperatures, 2021, Death Valley, CA", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)


plt.show()


