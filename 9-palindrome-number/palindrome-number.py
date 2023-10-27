class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        newX = str(x)[::-1]
        if newX == str(x):
            return True