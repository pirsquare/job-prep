


# In this example, backtrack()recursively adds numbers to current_permutation.
# When len(current_permutation)equals len(nums), a complete permutation is found.
# If a number is chosen ( used[i] = True), the function calls itself.
# After the recursive call returns, the choice is undone ( used[i] = False, current_permutation.pop()) to explore other possibilities.

# backtracking is just dfs
def generate_permutations(nums):
    result = []
    current_permutation = []
    used = [False] * len(nums)

    def backtrack():
        if len(current_permutation) == len(nums):
            result.append(list(current_permutation))
            return

        for i in range(len(nums)):
            if not used[i]:
                current_permutation.append(nums[i])
                used[i] = True
                backtrack()  # Explore with the new choice
                used[i] = False  # Backtrack: undo the choice
                current_permutation.pop() # Backtrack: remove from current permutation

    backtrack()
    return result

# Example usage:
print(generate_permutations([1, 2, 3]))
