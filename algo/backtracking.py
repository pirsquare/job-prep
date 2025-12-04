
# Backtracking often employs a depth-first search strategy to explore the solution space.

def find_subsets(nums):
    result = []
    current_subset = []

    def backtrack(index):
        # Base case: A subset is formed when we consider all elements
        if index == len(nums):
            result.append(list(current_subset)) # Append a copy
            return

        # Option 1: Include the current element
        current_subset.append(nums[index])
        backtrack(index + 1)
        current_subset.pop() # Backtrack: remove the current element

        # Option 2: Exclude the current element
        backtrack(index + 1)

    backtrack(0)
    return result

# Usage
nums = [1, 2, 3]
subsets = find_subsets(nums)
print(subsets)
