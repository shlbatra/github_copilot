# Original Code
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Comment, Context, Code
# - Provide a more readable version of the factorial function

# Generated Code

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)