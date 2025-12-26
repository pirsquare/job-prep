# Explanation:
# merge_sort(arr) function:
# Base Case: If the array has 0 or 1 element, it's already sorted, so return it.
# Divide: Calculate the middle index and split the array into left_half and right_half.
# Conquer: Recursively call merge_sort on both left_half and right_half to sort them.
# Combine: Call the merge function to combine the two sorted halves into a single sorted array.


# merge(left, right) function:
# This function takes two already sorted lists, left and right, and merges them into a single sorted result list.
# It uses two pointers, left_idx for left and right_idx for right, to compare elements.
# The smaller element is appended to result, and its respective pointer is incremented.
# After one list is exhausted, the remaining elements of the other list are appended to result.


def merge_sort(arr):
    if 1 >= len(arr):
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []
    left_idx = 0
    right_idx = 0

    # Compare elements from left and right halves and add to result
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Add remaining elements from left half (if any)
    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    # Add remaining elements from right half (if any)
    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    return result

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(my_list)
print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")
