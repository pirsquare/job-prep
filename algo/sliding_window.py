import math

# The sliding window technique is an optimization pattern used in algorithms, particularly for problems involving arrays or strings where you need to examine contiguous subarrays or substrings (windows) of a certain size. It aims to reduce time complexity, often from O(N²) to O(N), by avoiding redundant computations.

# Core Idea:
# Instead of re-calculating values for each new window from scratch, the sliding window technique maintains a window (defined by left and right pointers) and incrementally updates its state as it "slides" across the data. This means that when the window moves one step to the right, you remove the element at the left end of the old window and add the new element at the right end of the new window, efficiently updating any relevant calculations.

# Fixed-Size Window: The window always maintains a constant length.
# Example: Finding the maximum sum of a subarray of a fixed length k.
def max_subarray_sum(arr, k):
    if k > len(arr):
        return 0

    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]  # Add new element, remove old
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
k = 3
print(max_subarray_sum(arr, k)) # Output: 15 (from [4, 5, 6])


# Variable-Size Window: The window size can expand or contract based on certain conditions defined by the problem.
def variable_sliding_window(arr):
    left = 0  # Left pointer of the window
    right = 0 # Right pointer of the window
    # Initialize variables to store results or track conditions (e.g., max_length, current_sum, frequency_map)

    while len(arr) > right:
        # 1. Expand the window: Add the element at 'right' to the window's state
        #    Update any necessary variables (e.g., current_sum, frequency_map)

        # 2. Check condition and potentially shrink the window:
        #    While the current window violates a given condition (e.g., window_sum > target, too many distinct characters):
        #        Remove the element at 'left' from the window's state
        #        Update any necessary variables
        #        Increment 'left' pointer

        # 3. Process the current valid window (optional, depends on the problem):
        #    If the window meets the desired criteria, perform calculations or update results (e.g., max_length = max(max_length, right - left + 1))

        # 4. Move the right pointer to expand the window for the next iteration
        right += 1

    # Return the final result
    # return result


# Example: Finding the longest substring without repeating characters.
def longest_substring_without_repeating_characters(s):
    char_set = set()  # Stores characters in the current window
    left = 0          # Left pointer of the sliding window
    max_length = 0    # Stores the maximum length found so far

    for right in range(len(s)):
        # If the character at the right pointer is already in the set (duplicate)
        while s[right] in char_set:
            # Remove the character at the left pointer from the set
            char_set.remove(s[left])
            # Move the left pointer to the right
            left += 1

        # Add the current character (at the right pointer) to the set
        char_set.add(s[right])

        # Update the maximum length if the current window size is larger
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
s = "abcabcbb"
print(longest_substring_without_repeating_characters(s)) # Output: 3 (from "abc")


def min_subarray_len(target, nums):
    """
    Finds the minimum length of a contiguous subarray whose sum is >= target.

    Args:
        target: The target sum.
        nums: A list of positive integers.

    Returns:
        The minimum length of a subarray, or 0 if no such subarray exists.
    """
    left = 0
    current_sum = 0
    min_length = math.inf  # Initialize with a value larger than any possible length

    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink the window from the left while the sum is still >= target
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    # If min_length is still infinity, no valid subarray was found
    return min_length if min_length != math.inf else 0

# Example usage:
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(min_subarray_len(target, nums))  # Output: 2 (for the subarray [4, 3])
