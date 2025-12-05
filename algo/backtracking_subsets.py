
# Generating All Possible Subsets (Power Set):
# This involves finding all combinations of elements from a given collection, including the empty set and the collection itself. This is often achieved using recursion or backtracking:


# backtracking is just dfs
def find_subsets(nums):
    result = []
    current_subset = []

    def backtrack(index):
        # Add the current subset to the results
        result.append(list(current_subset))

        # Explore choices
        for i in range(index, len(nums)):
            # Make a choice: include the current number
            current_subset.append(nums[i])
            backtrack(i + 1)  # Recursively call for subsequent numbers

            # Backtrack: undo the choice (remove the current number)
            current_subset.pop()

    backtrack(0)
    return result

# Example usage:
numbers = [1, 2, 3]
subsets = find_subsets(numbers)
print(subsets)

