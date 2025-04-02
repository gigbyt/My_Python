import sys
sys.path.append('D:/My FILES (Sharable)/Python')  # Adjust the path to your package location
from My_Package import Arithmatical
n = int(input("What will be the the range? "))
Result = Arithmatical.fibonacci_numbers(n)
print(f"these are the first {n} terms : ") 
print(Result)