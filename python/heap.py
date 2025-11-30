import heapq

# heap/priority queue use cases
# Task and job scheduling. Like your OS, celery queue
# Customer support tickets. More critical issues handle first.

#===========================
# Heap (by default is Min)
# https://neetcode.io/problems/python-heap-push/question
#===========================
heap = [] # min heap
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)

print(heap[0])  # 1

heapq.heappush(heap, 0)

# print(heap[0])  #

# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))

# use heapify to transform existing list. remember that this is not full sorting
heap = [5, 7, 2, 13, 6, 5]
heapq.heapify(heap)

# heap is priority queue, not sort
print(heap) # [2, 6, 5, 13, 7, 5]

# but you can use nsmallest
print(heapq.nsmallest(4, heap))  # returns [2, 5, 5, 6]

print(heapq.heappop(heap)) # 2
print(heapq.heappop(heap)) # 5
print(heapq.heappop(heap)) # 5
print(heap) # [6, 13, 7]

while heap:
    print(heapq.heappop(heap))


#===========================
# Max Heap
# https://neetcode.io/problems/python-max-heap/question
#===========================
print("\n\nMax Heap")
nums = [4, 2, 3, 5]
max_heap = []

# no built-in max heap so use negative
for num in nums:
    heapq.heappush(max_heap, -num) # Negate the number

while max_heap:
    top = -heapq.heappop(max_heap) # Negate the number back
    print(top)


#===========================
# Custom Heap
# https://neetcode.io/problems/python-custom-heap/question
#===========================
# this use tuples to handle ordering
# first element of tuple is the comparison value, second element of tuple is the actual base value.

# let's get priority queue based on length of string
print("\n\nCustom Heap")
values = ['abcd', 'ab', 'a', 'abc']
print(f"Initial values: {values}")

heap = []
def transform_value(value):
    return len(value)

# use function to transform first comparison value
for value in values:
    pair = (transform_value(value), value)
    heapq.heappush(heap, pair)

while heap:
    pair = heapq.heappop(heap)
    print(pair[1])
