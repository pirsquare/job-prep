

# Longest Subarray With Sum = K
# Problem
# Return the maximum length of a subarray whose sum equals k.

# Input
nums = [1, -1, 5, -2, 3]
k = 3

def max_subarray_len(nums, k):
    prefix_index = {0: -1}
    curr_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        curr_sum += num

        if curr_sum - k in prefix_index:
            max_len = max(max_len, i - prefix_index[curr_sum - k])

        if curr_sum not in prefix_index:
            prefix_index[curr_sum] = i

    return max_len


print(max_subarray_len(nums, k))

