import hashlib
import os

lookup_table = {}

def hash_collision(k):
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')

    # Collision finding code goes here
    for value in range(100):

        random_binary = os.urandom(8)
        result = hashlib.sha256(random_binary).digest()
        result = result[:k]
        if result in lookup_table:
            print("Collission found")
            print("String 1: " + random_binary, "Matching bits: " + result[:k])
            print("String 2: " + lookup_table[result], "Matching bits: " + result[:k])
            x = random_binary
            y = lookup_table[result]
        else:
            lookup_table[result] = random_binary

#    x = b'\x00'
#    y = b'\x00'

    return (x, y)


if __name__ == '__hash_collission__':
    hash_collision(-3)
