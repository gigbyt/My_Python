n = int(input("Enter the number of times for repetitions: "))
for i in range(1, n+1):
    for a in range(1, i+1):
        print("*", end="")
    print()
