def fibonacci_numbers (n):
    fibonacci_seiries = [0, 1]
    while len(fibonacci_seiries) < n:
        fibonacci_seiries.append(fibonacci_seiries[-1] + fibonacci_seiries[-2])
    return fibonacci_seiries
n = int(input("What will be the the range? "))
Result = fibonacci_numbers(n)
print(f"these are the first {n} terms : ") 
print(Result)