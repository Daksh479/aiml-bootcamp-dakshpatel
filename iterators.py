# Read a big file without loading it
with open("large_file.txt", "w") as file:

    for i in range(1, 500001):
        file.write(
            f"This is line number {i}. Python is awesome.\n"
        )

print("File generated successfully!")

word = "Python"

total_lines = 0
matching_lines = 0

with open("large_file.txt", "r") as file:

    for line in file:

        total_lines += 1

        if word in line:
            matching_lines += 1

print("Total lines:", total_lines)
print("Lines containing word:", matching_lines)
