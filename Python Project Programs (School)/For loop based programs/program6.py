word = str(input("Enter any word or a sentence : "))
count = 0 
for i in word:
    if 'A' in i or 'a' in i or 'E' in i or 'e' in i or 'I' in i or 'i' in i or 'O' in i or 'o' in i or 'U' in i or 'u' in i :
        count += 1
print(f"The number of vowels is : {count}")