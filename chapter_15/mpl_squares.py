import matplotlib.pyplot as plt

"""Making the graph"""
input_values = [1, 2, 3, 4, 5]
square_nums = [1,4,9,16,25]

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()
ax.plot(input_values, square_nums, linewidth=3)


ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()