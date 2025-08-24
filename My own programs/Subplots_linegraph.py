import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [2,3,5,7,11]

plt.subplot(1,2,1)   # 1 row, 2 columns, plot 1
plt.plot(x, y1, color="blue")
plt.title("Squares")

plt.subplot(1,2,2)   # 1 row, 2 columns, plot 2
plt.plot(x, y2, color="red")
plt.title("Primes")

plt.show()
