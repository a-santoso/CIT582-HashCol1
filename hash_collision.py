import hashlib
import os
import sys

ref_table = {}


def hash_collision(k):

    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')

    # Collision finding code goes here
    for i in range(sys.maxsize):

        random_word = os.urandom(20)
        hash_result = hashlib.sha256(random_word).digest()
        hash_result = hash_result[:k]        # slice to last k digits
        if hash_result in ref_table:
            print("Collision found \n")
            print("Word 1 + Hash Result")
            print(random_word, hash_result)
            print("Word 2 + Hash Result")
            print(ref_table[hash_result], hash_result)
            x = random_word
            y = ref_table[hash_result]
            return (x, y)
        else:
            ref_table[hash_result] = random_word

if __name__ == '__main__':
    hash_collision(3)
