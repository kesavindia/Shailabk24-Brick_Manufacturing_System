#Implement a function to generate nth fibonnaci number

def fibonacci(n):
    if not isinstance(n,int):
        raise ValueError("Enter a valid numbers only.")
    elif n < 0:
        raise ValueError("Enter positive numbers only.")
    elif n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
try:
    n = int(input("Enter a number: "))
    fib_series = [fibonacci(i) for i in range(n)]
    print(fib_series)
except ValueError as e:
    print(f"Error:{e}")

