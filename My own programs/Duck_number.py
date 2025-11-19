flag = False
n = int(input("Enter a no: "))
while n>0:
    deg = n%10
    if deg == 0:
        print("duck no.")
        flag = True
        break
    n = n//10
if flag == False:
    print("Not a duck")