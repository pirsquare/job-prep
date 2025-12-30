from collections import deque

# Maximum sum subarray of size k (FIXED window)

# Question
# Given an array of integers, find the maximum sum of any contiguous subarray of size k.

# Input
nums = [2, 1, 5, 1, 3, 2]
k = 3

def max_sum_subarray(nums, k):
    window_sum = 0
    max_sum = 0
    max_window_items = []
    start = 0

    for i in range(k, len(nums)+1):
        window_items = nums[start:k+start]
        window_sum = sum(window_items)

        if window_sum > max_sum:
            max_sum = window_sum
            max_window_items = window_items

        start += 1
    return (max_sum, max_window_items)



print(max_sum_subarray(nums, k))
# 9  # subarray [5,1,3]
