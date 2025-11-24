s = input("Enter a string : ").strip()
vowels = set("aeiouAEIOU")
v = c = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
print(f"Number of vowels : {v}     Number of consonents : {c}")
