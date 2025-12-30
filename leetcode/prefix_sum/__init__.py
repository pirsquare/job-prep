

# What is Prefix Sum?

# Prefix Sum is a technique where you precompute cumulative sums so that range sum queries can be answered in O(1) time instead of O(n).
# Core Idea

# Given an array nums:
# nums = [2, 4, 6, 8]


# Build prefix sum:
# prefix = [0, 2, 6, 12, 20]


# Where:
# prefix[i] = sum(nums[0:i])

# Basic Prefix Sum Implementation
# def build_prefix_sum(nums):
#     prefix = [0]
#     for num in nums:
#         prefix.append(prefix[-1] + num)
#     return prefix
