

# Maximum sum subarray of size k (FIXED window)

# Question
# Given an array of integers, find the maximum sum of any contiguous subarray of size k.
# find max sum only (if find max sum equal k, use prefix sum)

# Input
nums = [2, 1, 5, 1, 3, 2]
k = 3

def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    start = 0

    for end in range(k, len(nums)):
        window_sum += nums[end]
        window_sum -= nums[start]
        start += 1
        max_sum = max(max_sum, window_sum)

    return max_sum



print(max_sum_subarray(nums, k))
# 9  # subarray [5,1,3]


