import random

class Solution:
    def __init__(self):
        alpha = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ")
        r_alpha = list(reversed(alpha))

        # Initialize encoding and decoding hashtables
        self.encrypt_hash={}
        self.decrypt_hash={}
        # create hashtable of enccoding to decoding items
        for i in range(len(alpha)):
            self.encrypt_hash[alpha[i]] = r_alpha[i]
            self.decrypt_hash[r_alpha[i]] = alpha[i]

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            j += 1  # skip '#'
            res.append(s[j:j + length])
            i = j + length

        return res