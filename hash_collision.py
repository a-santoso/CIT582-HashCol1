import hashlib
import os
import random
import binascii

lookup_table = {}


def hash_collision(k):

    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')

    # Collision finding code goes here
    for i in range(1000):

        random_binary = os.urandom(8)
        result = hashlib.sha256(random_binary).hexdigest()
        
#        result = bin(result)

        result = binascii.unhexlify(result)

        print("Result before: ")
        print(result)
        result = result[-k:]
        print("Result after: ")
        print(result)
        

        if result in lookup_table:
            print("Collision found")
            print(random_binary, result)
            print(lookup_table[result], result)

        else:
            lookup_table[result] = random_binary

    x = random_binary
    y = lookup_table[result]

    return (x, y)


if __name__ == '__main__':
    hash_collision(3)
