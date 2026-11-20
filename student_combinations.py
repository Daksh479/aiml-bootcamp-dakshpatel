# Given a list of 5 stude/nt names, generate every possible pair (using combination)
from itertools import combinations
students = ["asha", "ravi", "meera", "dev", "priya"]
pairs = list(combinations(students, 2))

print("All possible pairs:")
for pair in pairs:
    print(pair)

print("Total pairs:", len(pairs))

# # Given a list of 5 stude/nt names, generate every possible pair (using permutation)
from itertools import permutations
students = ["asha", "ravi", "meera", "dev", "priya"]
ordered_pairs = list(permutations(students, 2))

for pair in ordered_pairs:
    print(pair)

print("Total ordered pairs:", len(ordered_pairs))

# Use product to generate every combination of 3 shirt colours and 2 sizes.
from itertools import product
colours = ["Red", "Blue", "Black"]
sizes = ["Small", "Large"]
result = list(product(colours, sizes))

for item in result:
    print(item)

print("Total combinations:", len(result))