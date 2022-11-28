def find_duplicate(nums):
    if not isinstance(nums, list) or not all(
        isinstance(num, int) for num in nums
    ):
        return False

    nums.sort()

    for index, num in enumerate(nums[:-1]):
        if num == nums[index + 1] and num >= 0:
            return num

    return False
