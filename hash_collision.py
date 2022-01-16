import hashlib
import os
import sys

refTable = {}


def hash_collision(k):

    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')

    # Collision finding code goes here
    for i in range(sys.maxsize):

        random_binary = os.urandom(8)
        result = hashlib.sha256(random_binary).digest()
        result = result[:k]
        if result in refTable:
            print("Collision found")
            print(random_binary, result)
            print(refTable[result], result)

            x = random_binary
            y = refTable[result]
            return (x, y)

        else:
            refTable[result] = random_binary



if __name__ == '__main__':
    hash_collision(3)
