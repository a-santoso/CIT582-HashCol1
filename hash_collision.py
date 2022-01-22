import hashlib
import os
#import random
#import binascii
import sys

lookup_table = {}


def hash_collision(k):

    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')

    # Collision finding code goes here
    for i in range(sys.maxsize):             # Iterations to the MAX 

        random_binary = os.urandom(k)        # Generate k bytes of random words 
        result = hashlib.sha256(random_binary).hexdigest() # Compute SHA256 hashes for Hex
        result = int(result, 16)        # Convert Hex to Integer
        result = bin(result)            # Convert Integer to Bits


#        print("Result before: ")
#        print(result)
        result = result[-k:]            # Slice last k bits
#        print("Result after: ")
#        print(result)
        

        if result in lookup_table:
            print("Collision found")
            print(random_binary, result)
            print(lookup_table[result], result)
            break

        else:
            lookup_table[result] = random_binary

    x = random_binary
    y = lookup_table[result]
    
    print ("end")

    return (x, y)


if __name__ == '__main__':
    hash_collision(15)
