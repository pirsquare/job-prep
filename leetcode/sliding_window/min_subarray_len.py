# Minimum size subarray sum ≥ target (VARIABLE window)

# Question
# Find the minimum length of a contiguous subarray whose sum is ≥ target.

# Input
target = 7
nums = [2,3,1,2,4,3]


def min_subarray_len(target, nums):
    left = 0
    min_len = len(nums)
    window_items = []
    window_sum = 0

    for right in range(len(nums)):
        window_items.append(nums[right])
        window_sum = sum(window_items)

        while window_sum >= target:
            min_len = min(min_len, len(window_items))

            del window_items[0]
            window_sum = sum(window_items)
            left += 1

        print(f"left: {left}")
        print(f"right: {right}")
        print(f"window_items: {window_items}")

    return (min_len)


# recommended solution
def min_subarray_len(target, nums):
    left = 0
    window_sum = 0
    min_len = float("inf")

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1

    if min_len == float("inf"):
        return 0
    return min_len


print(min_subarray_len(target, nums))
# 2  # [4,3]
