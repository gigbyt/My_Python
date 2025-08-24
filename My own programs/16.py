import matplotlib.pyplot as plt

# Ages of students in a class
ages = [12, 13, 12, 14, 13, 12, 15, 14, 13, 12]

plt.hist(ages, bins=4, color="green", edgecolor="black")
plt.title("Age Distribution in Class")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.show()