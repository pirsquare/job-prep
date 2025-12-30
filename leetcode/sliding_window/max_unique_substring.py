from collections import deque


# Longest substring without repeating characters (VARIABLE window)

# Question
# Given a string s, find the length of the longest substring without repeating characters.

# Input
s = "abcabcbb"

def longest_unique_substring(string):
    max_len = 0
    seen = set()
    left = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right-left+1)

        print(f"left: {left}")
        print(f"right: {right}")
    return (max_len)



print(longest_unique_substring(s))
# 3  # "abc"


