def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num * num
    return total

# dev: How could we make this more efficient?
# copilot: You could use a list comprehension to make this more efficient.
# dev: How would that look?
# copilot: You could replace the for loop with a list comprehension like this:
# copilot: return sum([num * num for num in numbers])
# dev: Great idea! Let's try that.
# dev: Here's the updated code with the list comprehension.
# dev: Let's test it to make sure it works.
# dev: It works! Thanks for the suggestion.
# copilot: You're welcome! I'm glad I could help.