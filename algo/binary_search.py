

def binary_search(sorted_list, target):
    """
    Searches for a target value within a sorted list using binary search.

    Args:
        sorted_list: A list of elements sorted in ascending order.
        target: The value to search for.

    Returns:
        The index of the target value if found, otherwise -1.
    """
    low = 0
    high = len(sorted_list) - 1

    while high >= low:
        mid = int((low + high)/2)  # Calculate the middle index
        mid_value = sorted_list[mid]

        if mid_value == target:
            return mid  # Target found, return its index
        elif mid_value > target:
            high = mid - 1  # Target is in the left half
        else:  # target > mid_value
            low = mid + 1  # Target is in the right half

    return -1  # Target not found in the list


my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_found = 23
target_not_found = 100

print(f"Index of {target_found}: {binary_search(my_list, target_found)}")
print(f"Index of {target_not_found}: {binary_search(my_list, target_not_found)}")
