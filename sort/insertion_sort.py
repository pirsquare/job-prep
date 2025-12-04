

def insertion_sort(arr):
    """
    Sorts a list of elements using the Insertion Sort algorithm.

    Args:
        arr: The list to be sorted.
    """
    n = len(arr)

    # Traverse through 1 to n-1
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted
        j = i - 1     # Index of the last element in the sorted portion

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place the key in its correct position

# Example usage:
my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array is:", my_list)
