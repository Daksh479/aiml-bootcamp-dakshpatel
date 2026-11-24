# three functions: average(nums), biggest(nums), and is_prime(n)
def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

def biggest(nums):
    if not nums:
        return 0
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest

def is_prime(n):
    if not n <= 1:
        return False

    for i in range(2 , n):
        if n % i == 0:
            return False

    return True