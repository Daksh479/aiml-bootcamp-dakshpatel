# 1. Given a list of numbers, return the squares of only the odd ones.
l1 = list(range(1,20))
odd = filter(lambda x: x % 2 != 0, l1)
squares = list(map(lambda x: x ** 2, odd))
print(squares)

# 2. Given a list of names, return them uppercased and stripped of whitespace.
names =["  daksh", "python   ", "   codetrade   ", "  ai", "  ml"]
result = list(map(lambda names : names .strip().upper(), names))
print(result)

# 3. Given two lists of equal length, return a list of their pairwise products.
l1 = [2, 3, 4, 5]
l2 = [10, 20, 30, 40]
result = list(map(lambda x, y: x * y, l1, l2))
print(result)

# 4. Given a list of words, return only those longer than 4 characters.
words = ["apple", "cat", "banana", "dog", "python", "AI", "coding"]
result = list(filter(lambda word: len(word) > 4, words))
print(result)

# 5. Given a list of numbers, find the product of all of them (use reduce).
from functools import reduce
no =[2,3,4,5]
product = reduce(lambda x, y: x * y, no)
print(product)

# 6. Given a list of dicts with a "price" key, return the total price.
from functools import reduce
d1 = {
    "price1" : 10,
    "price2" : 20,
    "price3" : 30,
    "price4" : 40,
}
total_price = reduce(lambda x, y: x + y, d1.values())
print(total_price)

# 7. Given a nested list [[1,2],[3,4],[5]], flatten it to [1,2,3,4,5].
from functools import reduce
list = [[1, 2], [3, 4], [5]]
flatten = reduce(lambda x, y: x + y, list)
print(flatten)

# 8. Given a list of strings, return a dict mapping each to its length.
s1 = ["apple", "banana", "cherry", "date"]
length = dict(map(lambda x : (x, len(x)), s1))
print(length)

# 9. Given a list of mixed values, drop everything falsy (0, "", None, []).
mixed = [1,0,"",None,[]]
result = list(filter(None, mixed))
print(result)

# 10. Given a list of numbers, return the running total: [1,2,3] becomes [1,3,6].
from itertools import accumulate
numbers = [1, 2, 3]
running = list(accumulate(numbers))
print(running)
