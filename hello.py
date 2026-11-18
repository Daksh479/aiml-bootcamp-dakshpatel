# return the unique and sorted item

def unique(numbers):
    return sorted(set(numbers))


numbers = [5, 2, 8, 2, 1, 5, 9, 3, 1, 6, 6, 4, 1, 3]

result = unique(numbers)

print(result)