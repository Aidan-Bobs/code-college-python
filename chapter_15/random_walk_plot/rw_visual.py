import matplotlib.pyplot as plt
from random_walk import RandomWalk



while True:
    try:
        step_number = int(input("How many steps do you want to take? "))
    except ValueError:
        print("Please enter a number.")
        continue
    rw = RandomWalk(step_number, bias_x=False, bias_y=False, large_steps=False)
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(16, 6))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1, color="blue")
    ax.set_aspect('equal')

    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)


    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
