# Write fib_list(n) that returns the first n Fibonacci numbers as a list.
def fib_list(n):
    result = []

    a = 0
    b = 1

    for i in range(n):
        result.append(a)

        a, b = b, a + b

    return result

numbers = fib_list(10)

print(numbers)

#  Write fib_gen(n) that does the same with yield.

def fib_gen(n):
    a = 0
    b = 1

    for i in range(n):
        yield a

        a, b = b, a + b

numbers = fib_gen(10)

for num in numbers:
    print(num)