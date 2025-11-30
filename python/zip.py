

# zip lets you loop 2 list together at once
names = ['Alice', 'Bob', 'Charlie', 'David']
scores = [90, 85, 88, 92]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
