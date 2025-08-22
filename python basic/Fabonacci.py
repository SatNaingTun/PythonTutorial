def fibonacci(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        # Initialize the first two Fibonacci numbers
        # fn_minus_2 = 0  # FN(0)
        # fn_minus_1 = 1  # FN(1)
        for i in range(2, a+1):
            # fn = fn_minus_1 + fn_minus_2  # Calculate the next Fibonacci number
            # # Update the last two Fibonacci numbers
            # fn_minus_2 = fn_minus_1
            # fn_minus_1 = fn
            fn=fibonacci(a-1)+fibonacci(a-2)
        return fn

# Example usage
a = 8
print(f"Fibonacci number FN({a}) is {fibonacci(a)}")
