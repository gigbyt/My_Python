from all_func import *
p = int(input("Enter the PRINCIPAL AMOUNT : "))
r = int(input("Enter the RATE : "))
t = int(input("Enter the TIME PERIOD : "))
x = Ci(p, r, t)
y = Si(p, r, t)
print(f"Your si = {y} & ci = {x}")