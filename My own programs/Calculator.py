import sys
sys.path.append('D:/My FILES (Sharable)/Python')
from My_Package import Arithmatical

try:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    answer = str(input("What operation? ")).lower()  # Convert input to lowercase

    if answer == "addition":
        Result_sum = Arithmatical.add_numbers(number_1, number_2)
        print("Your sum is ", Result_sum)

    elif answer == "multiplication":
        Result_multiplied = Arithmatical.multiply_numbers(number_1, number_2)
        print("Your product is ", Result_multiplied)

    elif answer == "subtraction":
        Result_subtracted = Arithmatical.subtract_numbers(number_1, number_2)
        print("Your difference is ", Result_subtracted)

    elif answer == "division":
        if number_2 == 0:
            print("Undefined (cannot divide by zero)")
        else:
            Result_divided = Arithmatical.divide_numbers(number_1, number_2)
            print("Your quotient is ", Result_divided)

    else:
        print("Invalid operation (please write the operation name in all small letters)")

except ValueError:
    print("Invalid number input. Please enter integers only.")
except Exception as e:
    print(f"An error occurred: {e}")