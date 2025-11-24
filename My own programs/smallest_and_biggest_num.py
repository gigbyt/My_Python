A = []

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

if A:
    A.sort()
    print("Smallest number:", A[0])
    print("Largest number:", A[-1])
else:
    print("No numbers entered.")