t = (1, 'a', 3)               # create a tuple
r = []
print("tuple:", t)
print("length:", len(t))
print("first, last:", t[0], t[-1])
print("slice [1:]:", t[1:])   # slicing
a, b, *rest = t               # unpacking
print("unpacked a,b,rest:", a, b, rest)
print("concatenation:", t + ('x',))  # concatenation
print("repeat:", t * 2)       # repetition
