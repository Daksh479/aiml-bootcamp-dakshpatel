# 1. Create an array of the numbers 1 to 20. Then reverse it.
import numpy as np
a = np.arange(1 , 21)
print(a)
reverse = a[::-1]
print(reverse)

# 2. Create a 3×3 array of all zeros, then set the middle element to 1.
import numpy as np
arr = np.zeros((3 , 3))
print(arr)
arr[1,1] = 1
print(arr)

# 3. From np.arange(20), extract every third element.
import numpy as np
arr = np.arange(20)
print(arr)
result = arr[::3]
print(f"Every Third Element:{result}")

# 4. Given an array of 20 random integers, replace every odd number with -1.
import numpy as np
arr = np.arange(21)
print(arr)
arr[arr % 2 == 1] = -1
print(f"Replace odd one with -1:{arr}")

# 5. Find all elements of an array that are greater than the array's own mean.
import numpy as np
arr = np.array([10,20,30,40,50,60])
mean = np.mean(arr)
result = arr[arr > mean]
print(f"Mean:{mean}")
print(f"Element Greater than mean:{result}")

# 6. Count how many elements in an array are between 25 and 75 (inclusive).
import numpy as np
arr = np.arange(25 , 76)
print(arr)
count = np.sum((arr >= 25) & (arr <= 75))
print(f"Count of elements between 25 and 75: {count}")

# 7. Given a 1D array, return its 5 largest values, sorted descending.
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
largest_values = np.sort(arr)[-5:][::-1]
print(f"5 Largest Values (Descending): {largest_values}")

# 8. Swap the first and last rows of a 2D array.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Array:")
print(arr)
arr[[0, -1]] = arr[[-1, 0]]
print("Array after swapping first and last rows:")
print(arr)