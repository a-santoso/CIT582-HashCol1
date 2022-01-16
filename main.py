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
    for value in range(k):

        random_binary = os.urandom(8)
        result = hashlib.sha256(random_binary).digest()
        result = result[:1]
        if result in lookup_table:
            print("Collission")
            print(random_binary, result)
            print(lookup_table[result], result)
        else:
            lookup_table[result] = random_binary

    x = b'\x00'
    y = b'\x00'

    return (x, y)


if __name__ == '__main__':
    hash_collision(30)
