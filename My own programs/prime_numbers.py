def checkPrime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  for i in range(2, n):
    if n % i == 0:
      return False
  if n % i != 0:
    return True

n = int(input("Enter any number: "))
r = checkPrime(n)
if r == True:
  print("The number is prime")
else:
  print("The number is not prime")