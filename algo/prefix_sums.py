

def calculate_prefix_sum(arr):
    prefix_sum = [0]  # Initialize with a 0 for easier range sum calculation
    current_sum = 0
    for num in arr:
        current_sum += num
        prefix_sum.append(current_sum)
    return prefix_sum

# Example usage:
my_array = [3, 1, 4, 1, 5, 9, 2]
prefix_sums = calculate_prefix_sum(my_array)
print(f"Original array: {my_array}")
print(f"Prefix sum array: {prefix_sums}")
# Output:
# Original array: [3, 1, 4, 1, 5, 9, 2]
# Prefix sum array: [0, 3, 4, 8, 9, 14, 23, 25]
