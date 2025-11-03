class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        t = x[::-1]

        if t == x:
            return True
        else:
            return False