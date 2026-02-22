def sum_digits(n):
    n = abs(int(n))  
    n_str = str(n)   
    digit_sum = 0   

    for d in n_str:  
        if d.isdigit():  
            digit_sum += int(d)  
    return digit_sum  

if __name__ == "__main__":
    try:
        n = input("Enter a non-negative integer: ").strip()
        n = int(n)
        if n < 0:
            raise ValueError("The number must be non-negative.")
        print("Sum of digits:", sum_digits(n))
    except ValueError as e:
        print("Invalid input:", e)