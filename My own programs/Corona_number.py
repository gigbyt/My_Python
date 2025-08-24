flag = False
n = int(input("Enter any no. "))
while n>0:
    deg = n%10
    if deg % 2 != 0 :
        flag = True
    elif deg % 2 == 0:
        flag = False
        break
    n = n//10
if flag == True:
    print("Corona number")
elif flag == False:
    print("Vaccinated no.")
