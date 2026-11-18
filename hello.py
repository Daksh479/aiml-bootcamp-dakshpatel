#  function that returns the min, max, mean, and count — as a dict

def calculate(numbers):
    if not numbers:
        return {
            "min": None,
            "max": None,
            "mean": None,
            "count": 0
        }
    return {
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
        "count": len(numbers)
    }

numbers = [10, 20, 30, 40, 50]
result = calculate(numbers)
print(result)