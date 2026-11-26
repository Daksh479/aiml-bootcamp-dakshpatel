def average(nums: list[int]) -> float:

    if not nums:
        return 0.0

    return sum(nums) / len(nums)


def biggest(nums: list[int]) -> int:
    if not nums:
        return 0
    largest = nums[0]
    for num in nums:
        largest = max(largest, num)
    return largest


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
