


# A 3x3 matrix represented as a list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements:
# To access the element in the second row, third column (which is 6)
element = matrix[1][2]
print(f"Element at row 1, column 2 (0-indexed): {element}") # Output: 6
print()


# rows, then columns
rows = len(matrix)
cols = len(matrix[0]) if rows else 0

for r in range(rows):
    for c in range(cols):
        # Access element: matrix[r][c]
        print(f"Element at ({r}, {c}): {matrix[r][c]}")


# transposing matrix
transposed_matrix = [list(row) for row in zip(*matrix)]
print()
print("transposed_matrix")
print(transposed_matrix)
