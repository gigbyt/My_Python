import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]     # squares
y2 = [1, 8, 27, 64, 125]   # cubes

plt.plot(x, y1, label="Squares", color="blue", marker = "x")
plt.plot(x, y2, label="Cubes", color="green", marker = "o")

plt.title("Squares vs Cubes")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.legend()   # shows the labels
plt.show()