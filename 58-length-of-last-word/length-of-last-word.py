class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split s into a list containing only the words
        words = s.split()
        # Find the last word and get the length of it
        return len(words[-1])
        