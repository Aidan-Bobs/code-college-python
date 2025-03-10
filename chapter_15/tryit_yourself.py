import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('fivethirtyeight')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
ax1.scatter(x_values[:5], y_values[:5], c=y_values[:5], cmap='plasma', label="1st 5")
ax1.set_title("1st 5 points")
ax1.legend()


ax2.scatter(x_values, y_values, c=y_values, cmap='inferno', label="1st 5000")
ax2.set_title("1st 5000 points")
ax2.legend()

plt.tight_layout()
plt.show()