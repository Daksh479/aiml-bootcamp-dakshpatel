# 9. Create a 4×4 array containing the numbers 1 to 16 in order.
import numpy as np
arr = np.arange(1 , 17).reshape(4 , 4)
print(arr)

# 10. From that array, extract the second column, then the last two rows.
import numpy as np
arr = np.arange(1 , 17).reshape(4 , 4)
print(arr)
second_column = arr[:,1]
print(f"Second column:{second_column}")
last_rows =  arr[-2:, :]
print(f"Lat two rows:{last_rows}")

# 11. Compute the sum of each row, and separately the sum of each column.
import numpy as np
arr = np.arange(1, 17).reshape(4, 4)
print(arr)
row_sum = np.sum(arr, axis=1)
print("Row sum:", row_sum)
column_sum = np.sum(arr, axis=0)
print("Column sum:", column_sum)

# 12. Normalise a 2D array so every column has mean 0 and standard deviation 1.
import numpy as np
arr = np.array([
    [10, 20, 30],
    [20, 30, 40],
    [30, 40, 50],
    [40, 50, 60]
])
# Calculate mean of each column
mean = np.mean(arr, axis=0)

# Calculate standard deviation of each column
std = np.std(arr, axis=0)

# Normalize each column
normalized = (arr - mean) / std

print("Original array:")
print(arr)

print("\nNormalized array:")
print(normalized)

print("\nNew means:")
print(np.mean(normalized, axis=0))

print("\nNew standard deviations:")
print(np.std(normalized, axis=0))

# 13. Create a 5×5 array with 1s on the border and 0s inside.
import numpy as np
arr = np.ones((5, 5), dtype=int)
arr[1:-1, 1:-1] = 0
print(arr)

# 14. Given a 2D array, find the position (row, column) of the largest element.
import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 90, 60],
    [70, 80, 50]
])
index = np.argmax(arr)
position = np.unravel_index(index, arr.shape)
print("Largest element:", arr.max())
print("Position (row, column):", position)

# 15. Stack two 1D arrays into a 2D array — once as rows, once as columns.
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Stack as rows
row_stack = np.vstack((arr1, arr2))

# Stack as columns
col_stack = np.column_stack((arr1, arr2))

print("Stack as rows:")
print(row_stack)

print("\nStack as columns:")
print(col_stack)