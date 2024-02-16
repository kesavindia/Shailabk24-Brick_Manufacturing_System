# give all methods of dict
# Immutable object (int) - hashable
immutable_object = 42
hash_value = hash(immutable_object)

print(f"Object: {immutable_object}")
print(f"Hash Value: {hash_value}")

# Immutable objects (tuple) - hashable
immutable_tuple = (1, 2, 3)
hash_value_tuple = hash(immutable_tuple)
hash_value_tuple1 = hash(immutable_tuple)
print(f"Hash Value: {hash_value_tuple1}")
print(f"Hash Value: {hash_value_tuple}")
print(immutable_tuple)
# Mutable object (list) - not hashable
mutable_list = 'yuuui'

try:
    hash_value_list = hash(mutable_list)
except TypeError as e:
    print(f"TypeError: {e}")
