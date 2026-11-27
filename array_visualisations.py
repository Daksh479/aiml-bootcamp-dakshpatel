# • Create a 2D array of random values and display it with plt.imshow(). Add a colourbar.
import numpy as np
import matplotlib.pyplot as plt

# Create a 2D array of random values
arr = np.random.rand(5, 5)

# Display the array as an image
plt.imshow(arr ,cmap='gray')

# Add colourbar
plt.colorbar()

# Display the image
plt.show()

# • Create a gradient: a 2D array where values increase smoothly left-to-right. Display it.
import numpy as np
import matplotlib.pyplot as plt

# Create a gradient from 0 to 1
gradient = np.linspace(0, 1, 10)

# Repeat the gradient across 10 rows
arr = np.tile(gradient, (10, 1))

print(arr)

# Display gradient
plt.imshow(arr, cmap="gray")

plt.colorbar()
plt.title("Horizontal Gradient")

plt.show()

# • Create a checkerboard pattern using slicing and step indexing — no loops.
import numpy as np
import matplotlib.pyplot as plt

# Create a 10x10 array filled with zeros
arr = np.zeros((10, 10))

# Fill alternating positions with 1
arr[::2, ::2] = 1
arr[1::2, 1::2] = 1

# Display checkerboard
plt.imshow(arr, cmap="gray")

plt.title("Checkerboard Pattern")
plt.show()

# • Build a circle: for a grid of coordinates, mask the points within a radius of the centre. Display it.
import numpy as np
import matplotlib.pyplot as plt

# Create coordinate values
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

# Create coordinate grids
X, Y = np.meshgrid(x, y)

# Define centre and radius
radius = 5

# Create circular mask
circle = X**2 + Y**2 <= radius**2

# Display circle
plt.imshow(circle, cmap="gray", extent=[-10, 10, -10, 10])

plt.title("Circle using NumPy Masking")
plt.xlabel("X")
plt.ylabel("Y")

plt.colorbar()
plt.show()

# • Load or create a small greyscale image as an array. Print its shape and dtype. Slice out a quarter of it and
#   display just that.
import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 grayscale image
image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)

# Print image information
print("Image shape:", image.shape)
print("Image dtype:", image.dtype)

# Extract the top-left quarter
quarter = image[:50, :50]

print("Quarter shape:", quarter.shape)

# Display original and cropped image
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(quarter, cmap="gray")
plt.title("Top-left Quarter")

plt.show()

# • Flip the image vertically using only slicing.
import numpy as np
import matplotlib.pyplot as plt

# Create a grayscale image
image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)

# Flip vertically using slicing
flipped = image[::-1, :]

# Display original and flipped images
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(flipped, cmap="gray")
plt.title("Vertically Flipped Image")

plt.show()