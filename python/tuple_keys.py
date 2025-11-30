
# list can't be used as dict key, but tuples can!
# Tuple keys should be used in dictionaries when you need a composite key
# made of multiple, related values that are immutable and should not be changed.

# when to use tuple keys?
# Composite Identifiers like (first_name, last_name)
# Coordinates mapping (x, y)
# Network sockets like (ip_address, port)



dict_of_pairs = {}

dict_of_pairs[(0, 0)] = 1
dict_of_pairs[(0, 1)] = 2

print(dict_of_pairs)  # {(0, 0): 1, (0, 1): 2}

set_of_pairs = set()

set_of_pairs.add((0, 0))
set_of_pairs.add((0, 1))

print(set_of_pairs)  # {(0, 0), (0, 1)}
