a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Which type of operation do you want: 1 -> a/b 2-> b/a : "))
d = int(input("Which type of operation do you want: 1 -> a-b 2-> b-a : "))

if c == 1 :
    print(f"Quotient of the two numbers is {a/b}")
    print(f"floor Division of the two numbers is {a//b}")
else : 
    print(f"Quotient of the two numbers is {b/a}")
    print(f"floor Division of the two numbers is {a//b}")

if d == 1 :
    print(f"Difference of the two numbers is {a-b}")
else : 
    print(f"Difference of the two numbers is {b-a}")
    
print(f"Sum of the two numbers is {a+b}")

print(f"Product of the two numbers is {a*b}")

print(f"Exponential product of the two numbers is {a**b}")
