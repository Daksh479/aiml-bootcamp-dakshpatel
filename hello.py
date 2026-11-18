# FizzBuzzBuzz (new version)

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0 and 1 % 7 == 0:
        print("FizzBuzzBuzz")

    elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    elif i % 7 == 0:
         print("Buzz")

    else:
        print(i)