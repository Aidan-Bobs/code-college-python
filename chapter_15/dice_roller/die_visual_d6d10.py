import plotly.express as px
import pandas as pd

from die import Die

# Create a D6 and D10.
die_1 = Die()
die_2 = Die(10)
# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(50000)]


#analisis
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies=[results.count(value) for value in poss_results]

bar_data_frame = pd.DataFrame({"Result": poss_results, "Frequency": frequencies})

fig = px.bar(bar_data_frame,x="Result", y="Frequency", title="Frequency analysis of rolling a D6 & D10")

fig.update_layout(xaxis_dtick=1)

fig.show()
