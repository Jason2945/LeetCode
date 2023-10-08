class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        # Find the smallest word in strs
        shortest_word = min(strs, key=len)
        
        # Get the length of the shortest word and use it as the index to test for all words in strs
        for word_index in range(len(shortest_word)):
            # Check each worth in strs
            for word in strs:
                # If the letter doesn't match the shortest word's index, return the current common prefix
                if word[word_index] != shortest_word[word_index]:
                    return common_prefix
            # If it matches, add the current word_index into common prefix and test the next letter
            common_prefix += shortest_word[word_index]
        # Return common prefix after all the test is done
        return common_prefix

        