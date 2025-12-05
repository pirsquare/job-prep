

# converging pointers
def find_pair_with_sum(arr, target_sum):
    """
    Finds if a pair in a sorted array sums to the target_sum.

    Args:
        arr: A sorted list of integers.
        target_sum: The integer target sum.

    Returns:
        True if such a pair exists, False otherwise.
    """
    left = 0  # Initialize left pointer at the beginning of the array
    right = len(arr) - 1  # Initialize right pointer at the end of the array

    while right > left:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            return True  # Found the pair
        elif target_sum > current_sum:
            left += 1  # Move left pointer to increase the sum
        else:  # current_sum > target_sum
            right -= 1  # Move right pointer to decrease the sum

    return False  # No such pair found

# Test cases
print(find_pair_with_sum([1, 2, 3, 4, 5], 7))  # Output: True (2 + 5 = 7)
print(find_pair_with_sum([1, 2, 3, 4, 5], 10)) # Output: False
print(find_pair_with_sum([-3, -1, 0, 1, 2], -2)) # Output: True (-3 + 1 = -2)
print(find_pair_with_sum([], 5)) # Output: False
