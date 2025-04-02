n = int(input("Enter a number: "))
count = 0 
while count < n:
    count += 1
    if count == 3:
        continue
    print(f"Current count : {count}")
print("Loop finished")