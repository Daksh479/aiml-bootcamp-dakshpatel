# Given a list of numbers, use a comprehension to return only the even ones, each doubled.

def even(numbers):
    return [x * 2 for x in numbers if x % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = even(numbers)

print(result)
