import matplotlib.pyplot as plt

# Hours studied vs Marks obtained
hours = [1, 2, 3, 4, 5, 6, 7]
marks = [40, 50, 55, 65, 70, 75, 80]

plt.scatter(hours, marks, color="purple", marker="x")
plt.title("Hours Studied vs Marks Obtained")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()