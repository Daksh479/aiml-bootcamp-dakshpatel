# while loop
numbers = [1, 2, 3]

iterator = iter(numbers)

while True:
    try:
        x = next(iterator)
        print(x)

    except StopIteration:
        break
