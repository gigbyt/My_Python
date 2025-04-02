n = int(input("Enter the number of times the pattern should be repeated: "))
for i in range(1, n+1):
    for a in range (n, i, -1):
        print(i, end=" ")
    print()
