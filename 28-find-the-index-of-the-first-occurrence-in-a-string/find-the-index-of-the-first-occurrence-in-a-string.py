class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Make sure the length of haystack is longer than the length of the needle.
        # You only need to check when the needle can still fit in the haystack
        #IE if needle has 7 letters and haystack has 3 letters left, it won't fit the needle so no need to check
        for index in range(len(haystack) - len(needle) + 1):
            #Check that haystack to the length to the length of the needle if is there, return the first index appeared
            if haystack[index : index+len(needle)] == needle:
                return index
        return -1
        