

# Longest Subarray With Sum = K
# Problem
# Return the maximum length of a subarray whose sum equals k.
# find max sum length equal k (if only find max sum, no tracking, use sliding window)

# Input
nums = [1, -1, 5, -2, 3]
k = 3

def max_subarray_len(nums, k):
    seen = {0: -1}   # prefix_sum -> earliest index
    prefix = 0
    best = 0

    for i, num in enumerate(nums):
        prefix += num

        if prefix - k in seen:
            best = max(best, i - seen[prefix - k])

        # keep earliest index only
        if prefix not in seen:
            seen[prefix] = i

    return best


print(max_subarray_len(nums, k))

