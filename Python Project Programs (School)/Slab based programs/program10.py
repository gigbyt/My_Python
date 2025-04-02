a = int(input("Distance traveled: "))
if a >= 1 and a <= 100:
    fare = a * 15    
elif a >= 100 and a <= 200:
    fare = 100 * 15 + (a - 100) * 17 
elif a >= 200:
    fare = 100 * 15 + 100 * 17 + (a - 100) * 20 
print (f"Final Fare = {fare}")