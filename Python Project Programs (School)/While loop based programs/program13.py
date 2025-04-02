n = int(input("Enter any number : "))
sum = 0 
prod = 1
while n > 0:
    deg = n % 10
    sum += deg
    prod *= deg
    n = n // 10
if sum == prod :
    print("The Number enetered is a spy number.")
else:
    print("The Number enetered is not a spy number.")