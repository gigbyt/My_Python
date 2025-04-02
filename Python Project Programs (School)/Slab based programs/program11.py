a  = int(input("What is your basic salary : "))
if a >= 1 and a <= 100000:
    DA = (0.08 * a) + a
    HRA = (0.05 * a) + a
    Tax = (0.03 * a) + a
    print(f"₹{DA + HRA - Tax} is your net salary.")
elif a >= 100000 and a <= 200000:
    DA = (0.12 * a) + a
    HRA = (0.08 * a) + a
    Tax = (0.05 * a) + a
    print(f"₹{DA + HRA - Tax} is your net salary.")
elif a > 200000:
    DA = (0.15 * a) + a
    HRA = (0.12 * a) + a
    Tax = (0.7 * a) + a
    print(f"₹{DA + HRA - Tax} is your net salary.")