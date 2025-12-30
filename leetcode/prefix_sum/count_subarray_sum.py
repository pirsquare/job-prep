

# Count Subarrays With Sum = K
# Subarray sum equals K
# Problem
# Given an integer array nums and an integer k, return the number of contiguous subarrays whose sum equals k.
# A contiguous subarray is a continuous slice of an array.

# Input
nums = [2,2,2,4,4]
k = 4

def subarray_sum(nums, k):
    count = 0
    curr_sum = 0

    # seen = {prefix_sum: frequency}
    # A prefix sum is the sum of elements from the start of the array up to the current index
    seen = {0: 1}

    for num in nums:
        curr_sum += num

        # How many times have we previously seen a prefix sum equal to curr_sum - k?
        # curr_sum - previous_sum = k
        # subarray sum = k
        count += seen.get(curr_sum - k, 0)
        seen[curr_sum] = seen.get(curr_sum, 0) + 1

    print(f"seen: {seen}")
    # seen: {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    return count


print(subarray_sum(nums, k))
# 4
