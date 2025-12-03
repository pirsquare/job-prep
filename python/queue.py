from collections import deque

# deque (pronounced "deck")
# Double-Ended Operations: Deques allow for efficient append, pop, appendleft, and popleft operations, offering approximately O(1) time complexity for these actions. This contrasts with standard Python lists, where inserting or deleting at the beginning can be an O(N) operation.

# Generalization of Stacks and Queues: Deques can effectively implement both stack-like (LIFO - Last In, First Out) and queue-like (FIFO - First In, First Out) behaviors due to their double-ended nature.


# Create a deque
my_deque = deque([1, 2, 3])
print(f"Initial deque: {my_deque}")

# Append to the right
my_deque.append(4)
print(f"After append(4): {my_deque}")

# Append to the left
my_deque.appendleft(0)
print(f"After appendleft(0): {my_deque}")

# Pop from the right
popped_right = my_deque.pop()
print(f"Popped from right: {popped_right}, Deque: {my_deque}")

# Pop from the left
popped_left = my_deque.popleft()
print(f"Popped from left: {popped_left}, Deque: {my_deque}")

# Deque with a maxlen
fixed_size_deque = deque(maxlen=3)
fixed_size_deque.append(1)
fixed_size_deque.append(2)
fixed_size_deque.append(3)
print(f"Fixed size deque: {fixed_size_deque}")
fixed_size_deque.append(4) # 1 is automatically removed from the left
print(f"After appending 4 to full deque: {fixed_size_deque}")
