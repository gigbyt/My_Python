P = int(input("Enter your percentage : "))
if P >= 0 and P <= 40:
    print("You got Grade D ;( ")
elif P >= 41 and P <= 60:
    print("You got Grade C :|")
elif P >= 61 and P <= 80:
    print("You got Grade B :)")
elif P >= 81 and P <= 100:
    print("You got Grade A :D")
else:
    print("invalid")