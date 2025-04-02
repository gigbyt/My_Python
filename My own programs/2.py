n = int(input("Enter any number: "))
for i in range(1, n+1):
    R = n % i
    if R == 0:
        print(f"{i}")
