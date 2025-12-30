

# Question 1: Range Sum Queries (Immutable)

# Problem
# You are given an integer array nums and q queries.
# Each query contains two integers l and r.

# Return the sum of elements from index l to r (inclusive).

# Constraints
# 1 ≤ n, q ≤ 10^5
# -10^4 ≤ nums[i] ≤ 10^4

# Input
nums = [1, 2, 3, 4, 5]
queries = [(0,2), (1,3)]

def range_sum(nums, queries):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    print(f"prefix: {prefix}")

    result = []
    for l, r in queries:
        result.append(prefix[r + 1] - prefix[l])
    return result

print(range_sum(nums, queries))

