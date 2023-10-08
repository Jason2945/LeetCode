class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check to make sure the needle is in the haystack
        if needle in haystack:
            index = haystack.find(needle)
            return index
        else :
            return -1
        