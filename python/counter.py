from collections import Counter


# basicially converts list into dict. Each distinct value mapped to number of counts
nums = [1, 2, 4, 3, 2, 1]

counter = Counter(nums)

print(counter)  # Counter({1: 2, 2: 2, 4: 1, 3: 1})

counter[100] += 1 # No error, even though 100 is not a key

print(counter)  # Counter({1: 2, 2: 2, 4: 1, 3: 1, 100: 1})
