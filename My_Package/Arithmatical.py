def add_numbers(n1, n2):
    try:
        Result_sum = n1 + n2
        return Result_sum
    except Exception as e:
        return ("invalid input")


def multiply_numbers(n1, n2):
    try:    
        Result_multiplied = n1 * n2
        return Result_multiplied
    except Exception as e:
        return ("invalid input")


def subtract_numbers(n1, n2):
    try:
        if n1 > n2:
            Result_subtracted = n1 - n2
        elif n1 < n2:
            Result_subtracted = n2 - n1
        return Result_subtracted
    except Exception as e:
        return ("invalid input")


def divide_numbers(n1, n2):
    try:
        if n1 > n2:
            Result_divided = n1 / n2
        elif n1 < n2:
            Result_divided = n2 / n1
        elif n1 == 0 or n2 == 0:
            print("Undefined")
        return Result_divided
    except Exception as e:
        print("invalid input")

def fibonacci_numbers (n):
    fibonacci_seiries = [0, 1]
    while len(fibonacci_seiries) < n:
        fibonacci_seiries.append(fibonacci_seiries[-1] + fibonacci_seiries[-2])
    return fibonacci_seiries