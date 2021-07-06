#!/usr/bin/env python

# A Python implementation of the block cipher IDEA

# Copyright (c) 2015 Bo Zhu https://about.bozhu.me
# MIT License
import gmpy2

def _mul(x, y):
    assert 0 <= x <= 0xFFFF
    assert 0 <= y <= 0xFFFF

    if x == 0:
        x = 0x10000
    if y == 0:
        y = 0x10000

    r = (x * y) % 0x10001

    if r == 0x10000:
        r = 0

    assert 0 <= r <= 0xFFFF
    return r


def _KA_layer(x1, x2, x3, x4, round_keys):
    assert 0 <= x1 <= 0xFFFF
    assert 0 <= x2 <= 0xFFFF
    assert 0 <= x3 <= 0xFFFF
    assert 0 <= x4 <= 0xFFFF
    z1, z2, z3, z4 = round_keys[0:4]
    assert 0 <= z1 <= 0xFFFF
    assert 0 <= z2 <= 0xFFFF
    assert 0 <= z3 <= 0xFFFF
    assert 0 <= z4 <= 0xFFFF

    y1 = _mul(x1, z1)
    y2 = (x2 + z2) % 0x10000
    y3 = (x3 + z3) % 0x10000
    y4 = _mul(x4, z4)

    return y1, y2, y3, y4


def _MA_layer(y1, y2, y3, y4, round_keys):
    assert 0 <= y1 <= 0xFFFF
    assert 0 <= y2 <= 0xFFFF
    assert 0 <= y3 <= 0xFFFF
    assert 0 <= y4 <= 0xFFFF
    z5, z6 = round_keys[4:6]
    assert 0 <= z5 <= 0xFFFF
    assert 0 <= z6 <= 0xFFFF

    p = y1 ^ y3
    q = y2 ^ y4

    s = _mul(p, z5)
    t = _mul((q + s) % 0x10000, z6)
    u = (s + t) % 0x10000

    x1 = y1 ^ t
    x2 = y2 ^ u
    x3 = y3 ^ t
    x4 = y4 ^ u

    return x1, x2, x3, x4


class IDEA:
    def __init__(self, key):
        self._keys = None
        self.change_key(key)

    def change_key(self, key):
        assert 0 <= key < (1 << 128)
        modulus = 1 << 128

        sub_keys = []
        for i in range(9 * 6):
            sub_keys.append((key >> (112 - 16 * (i % 8))) % 0x10000)
            if i % 8 == 7:
                key = ((key << 25) | (key >> 103)) % modulus

        keys = []
        for i in range(9):
            round_keys = sub_keys[6 * i: 6 * (i + 1)]
            keys.append(tuple(round_keys))
        self._keys = tuple(keys)

    def encrypt(self, plaintext):
        assert 0 <= plaintext < (1 << 64)
        x1 = (plaintext >> 48) & 0xFFFF
        x2 = (plaintext >> 32) & 0xFFFF
        x3 = (plaintext >> 16) & 0xFFFF
        x4 = plaintext & 0xFFFF

        for i in range(8):
            round_keys = self._keys[i]

            y1, y2, y3, y4 = _KA_layer(x1, x2, x3, x4, round_keys)
            x1, x2, x3, x4 = _MA_layer(y1, y2, y3, y4, round_keys)

            x2, x3 = x3, x2

        # Note: The words x2 and x3 are not permuted in the last round
        # So here we use x1, x3, x2, x4 as input instead of x1, x2, x3, x4
        # in order to cancel the last permutation x2, x3 = x3, x2
        y1, y2, y3, y4 = _KA_layer(x1, x3, x2, x4, self._keys[8])

        ciphertext = (y1 << 48) | (y2 << 32) | (y3 << 16) | y4
        return ciphertext

def my_encrypt(plaintext, round_keys):
    assert 0 <= plaintext < (1 << 64)
    x1 = (plaintext >> 48) & 0xFFFF
    x2 = (plaintext >> 32) & 0xFFFF
    x3 = (plaintext >> 16) & 0xFFFF
    x4 = plaintext & 0xFFFF

    y1, y2, y3, y4 = _KA_layer(x1, x2, x3, x4, round_keys)
    x1, x2, x3, x4 = _MA_layer(y1, y2, y3, y4, round_keys)

    x2, x3 = x3, x2

    y1, y2, y3, y4 = x1, x2, x3, x4
    ciphertext = (y1 << 48) | (y2 << 32) | (y3 << 16) | y4
    return ciphertext

def encipher(plaintext, round_keys):
    x2 = plaintext[0] & 0xFFFF
    x1 = (plaintext[0] >> 16) & 0xFFFF
    x4 = plaintext[1] & 0xFFFF
    x3 = (plaintext[1] >> 16) & 0xFFFF

    y1, y2, y3, y4 = _KA_layer(x1, x2, x3, x4, round_keys)
    x1, x2, x3, x4 = _MA_layer(y1, y2, y3, y4, round_keys)

    x2, x3 = x3, x2

    y1, y2, y3, y4 = x1, x2, x3, x4
    # ciphertext = (y1 << 48) | (y2 << 32) | (y3 << 16) | y4
    d = [0, 0]
    d[0] = (x2 & 0xffff) | ((x1 & 0xffff) << 16)
    d[1] = (x4 & 0xffff) | ((x3 & 0xffff) << 16)
    return d

def my_decrypt(ciphertext, round_keys):
    assert 0 <= ciphertext < (1 << 64)
    x1 = (ciphertext >> 48) & 0xFFFF
    x2 = (ciphertext >> 32) & 0xFFFF
    x3 = (ciphertext >> 16) & 0xFFFF
    x4 = ciphertext & 0xFFFF

    x2, x3 = x3, x2
    x1, x2, x3, x4 = _MA_layer(x1, x2, x3, x4, round_keys)
    y1, y2, y3, y4 = _KA_layer(x1, x2, x3, x4, round_keys)
    ciphertext = (y1 << 48) | (y2 << 32) | (y3 << 16) | y4
    return ciphertext

def decipher(ciphertext, round_keys):
    x2 = ciphertext[0] & 0xFFFF
    x1 = (ciphertext[0] >> 16) & 0xFFFF
    x4 = ciphertext[1] & 0xFFFF
    x3 = (ciphertext[1] >> 16) & 0xFFFF

    x2, x3 = x3, x2
    x1, x2, x3, x4 = _MA_layer(x1, x2, x3, x4, round_keys)
    y1, y2, y3, y4 = _KA_layer(x1, x2, x3, x4, round_keys)
    # ciphertext = (y1 << 48) | (y2 << 32) | (y3 << 16) | y4
    d = [0, 0]
    d[0] = (y2 & 0xffff) | ((y1 & 0xffff) << 16)
    d[1] = (y4 & 0xffff) | ((y3 & 0xffff) << 16)
    return d

def main():

    plain = 0xF129A6601EF62A47
    rk = [1,2,3,4,5,6]
    cipher = my_encrypt(plain, rk)
    print(hex(cipher))

    irk = [int(gmpy2.invert(rk[0], 0x10001)), 0x10000-rk[1], 0x10000-rk[2], int(gmpy2.invert(rk[3], 0x10001)), rk[4], rk[5]]
    ppp = my_decrypt(cipher, irk)

    print(irk)
    print(hex(plain))
    print(hex(ppp))

    assert ppp == plain

    p1 = [0xdeadbeef, 0xcaa0ffee]
    rk = [7,6,5,4,3,2]
    d1 = encipher(p1, rk)
    irk = [int(gmpy2.invert(rk[0], 0x10001)), 0x10000 - rk[1], 0x10000 - rk[2], int(gmpy2.invert(rk[3], 0x10001)),
           rk[4], rk[5]]
    p2 = decipher(d1, irk)

    assert p1[0] == p2[0] and p1[1] == p2[1]



if __name__ == '__main__':
    main()
