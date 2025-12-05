
# Kadane's Algorithm is an efficient method used to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers. It is a dynamic programming approach that operates in linear time complexity, O(N).

def maxSubArraySum(arr):
    """
    Calculates the maximum sum of a contiguous subarray using Kadane's Algorithm.

    Args:
        arr: A list of numbers (integers or floats).

    Returns:
        The maximum sum of a contiguous subarray.
    """
    if not arr:
        return 0  # Or raise an error for an empty array

    max_so_far = arr[0]  # Stores the maximum sum found globally
    current_max = arr[0] # Stores the maximum sum ending at the current position

    for i in range(1, len(arr)):
        # Decide whether to extend the current subarray or start a new one
        current_max = max(arr[i], current_max + arr[i])

        # Update the overall maximum sum if the current_max is greater
        max_so_far = max(max_so_far, current_max)

    return max_so_far

# Example usage:
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maximum subarray sum for {nums1}: {maxSubArraySum(nums1)}")

nums2 = [1]
print(f"Maximum subarray sum for {nums2}: {maxSubArraySum(nums2)}")

nums3 = [5, 4, -1, 7, 8]
print(f"Maximum subarray sum for {nums3}: {maxSubArraySum(nums3)}")

nums4 = [-1, -2, -3]
print(f"Maximum subarray sum for {nums4}: {maxSubArraySum(nums4)}")
