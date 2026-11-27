# • Create a (3, 4) array and a (4,) array. Add them. Explain in a comment why it works.
import numpy as np
arr1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
arr2 = np.array([10, 20, 30, 40])
result = arr1 + arr2
print(result)
print("Shape:", result.shape)

# • Create a (3, 4) array and a (3,) array. Add them. It fails — read the error and write down what shapes NumPy compared.
import numpy as np
arr1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
arr2 = np.array([10, 20, 30])

result = arr1 + arr2

print(result)

# • Fix that failure with reshape. Explain what the reshape changed.
import numpy as np
arr1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
arr2 = np.array([10, 20, 30])

# Reshape the second array
arr2 = arr2.reshape(3, 1)

result = arr1 + arr2

print(result)
print("First array shape:", arr1.shape)
print("Second array shape:", arr2.shape)
print("Result shape:", result.shape)
# • Add a (3, 1) array to a (1, 4) array. Predict the output shape before running it. Were you right?
import numpy as np
arr1 = np.array([
    [1],
    [2],
    [3]
])
arr2 = np.array([
    [10, 20, 30, 40]
])

result = arr1 + arr2

print(result)
print("Shape:", result.shape)

# • Use broadcasting to build a 10×10 multiplication table without any loops.
import numpy as np

arr1 = np.arange(1, 11).reshape(10, 1)

arr2 = np.arange(1, 11).reshape(1, 10)

result = arr1 * arr2

print(result)
print("Shape:", result.shape)

# • Use broadcasting to compute the distance from every point in a set to a single reference point.
import numpy as np

# Collection of points
points = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
])

# Single reference point
reference = np.array([0, 0])

# Calculate distances using broadcasting
difference = points - reference

squared = difference ** 2

sum_squared = np.sum(squared, axis=1)

distances = np.sqrt(sum_squared)

print("Points:")
print(points)

print("\nReference point:")
print(reference)

print("\nDistances:")
print(distances)