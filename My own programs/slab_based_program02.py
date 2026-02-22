n = int(input("ENTER A NUMBER - "))
try:
    if n%2 != 0:
        print("Wierd")
    elif n % 2 == 0:
        if n >= 2 and n <= 5:
            print("Not Wierd")
        elif n>=6 and n<=20:
            print("Not Wierd")
        elif n>20:
            print("Not Wierd")
except TypeError as t:
    print("Wrong Input type!")