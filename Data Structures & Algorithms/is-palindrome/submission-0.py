class Solution:
    def remove_non_alnum(self, s: str) -> str:
        # Time: O(N), Space: O(N)
        return "".join(char.lower() for char in s if char.isalnum())

    def isPalindrome(self, s: str) -> bool:
        st = self.remove_non_alnum(s)
        l = 0
        r = len(st) - 1

        while l < r:
            if st[l] != st[r]:
                return False;

            l += 1
            r -=1

        return True          
