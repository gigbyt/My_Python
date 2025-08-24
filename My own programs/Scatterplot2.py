import matplotlib.pyplot as plt

sleep = [4,5,6,7,8]
energy = [3,4,6,7,9]

plt.scatter(sleep, energy, color="red", marker="o")
plt.title("Sleep vs Energy")
plt.xlabel("Hours of Sleep")
plt.ylabel("Energy Level")

plt.legend()
plt.show()