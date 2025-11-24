A=[]
while True:
    item = input("Enter an integer to add (or press Enter to finish): ").strip()
    if item == "":
        break
    try:
        item = int(item)
    except ValueError:
        print("Not an integer, try again.")
        continue
    A.append(item)
    print("Added:", item)

print(f"Final list is: {A}")
print (f"Sum: {sum(A)}   Min: {min(A)}   Max: {max(A)}")