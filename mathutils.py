
"""Provide utility functions for basic mathematical operations."""


from pyparsing import nums


def average(nums: list[float]) -> float:
    """Return the average of a list of numbers.

    Args:
        nums (list): A list of numeric values.

    Returns:
        float or int: The average of the numbers.
            Returns 0 if the list is empty.
    """
    if not nums:
        return 0

    return sum(nums) / len(nums)


def biggest(nums: list[float]) -> float:
    """Return the largest number from a list.

    Args:
        nums (list): A list of numeric values.

    Returns:
        int or float: The largest number in the list.
            Returns 0 if the list is empty.
    """
    if not nums:
        return 0

    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest


def is_prime(n):
    """Return whether a number is prime.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if the number is prime, otherwise False.
            Numbers less than or equal to 1 are not prime.
    """
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
