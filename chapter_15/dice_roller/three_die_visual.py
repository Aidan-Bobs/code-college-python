import plotly.express as px
import pandas as pd

from die import Die

# Create a D6.
die_1 = Die()
die_2 = Die()
die_3 = Die()
# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() + die_3.roll() for _ in range(1000)]


#analisis
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+1)
frequencies=[results.count(value) for value in poss_results]

bar_data_frame = pd.DataFrame({"Result": poss_results, "Frequency": frequencies})

fig = px.bar(bar_data_frame,x="Result", y="Frequency", title="Dice Roll Frequency Analysis of Three Dice")

fig.update_layout(xaxis_dtick=1)

fig.show()
