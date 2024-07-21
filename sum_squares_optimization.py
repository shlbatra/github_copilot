# Original Code
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num * num
    return total

# Comment, Context, Code
# - Optimize the sum_of_squares function using a list comprehension

# Generated Code

def sum_of_squares(numbers):
    return sum([num * num for num in numbers])