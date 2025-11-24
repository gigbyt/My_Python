s = input("Enter a string: ")
chars = []
for ch in s:
    if ch.isalpha():
        lower_ch = ch.lower()
        chars.append(lower_ch)
clean = ''.join(chars)
print("Cleaned string:", clean)
if not clean:
    print("NO")
else:
    if clean == clean[::-1]:
        print("YES")
    else:
        print("NO")