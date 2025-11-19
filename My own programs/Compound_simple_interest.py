import sys
sys.path.append('D:/My FILES (Sharable)/Python')
from My_Package import Money

P = int(input("Enter the principal amount: "))
R = int(input("Enter the rate of interest: "))
T = int(input("Enter the time period in years: "))
type = str(input("Enter the type of interest (si/ci): ")).lower()

x = Money.interest(P, R, T, type)
print(x)
