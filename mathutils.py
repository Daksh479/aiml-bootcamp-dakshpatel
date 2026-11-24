from typing import Optional

def average(nums: list[int]) -> Optional[float]:
    if not nums:
        return 0.0

    return sum(nums) / len(nums)


def biggest(nums: list[int]) -> Optional[int]:
    if not nums:
        return None

    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest


def is_prime(n: int) -> Optional[bool]:
    if n <= 1:
        return None

    for i in range(2, n):
        if n % i == 0:
            return None

    return True
