class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined_word = ""
        # Check to saee which word is longer
        if len(word1) > len(word2):
            for index in range(len(word1)):
                combined_word += word1[index]
                # Skip the shorter word once there are none left
                try:
                    combined_word += word2[index]
                except IndexError:
                    pass
                
        else :
            for index in range(len(word2)):
                try:
                    combined_word += word1[index]
                except IndexError:
                    pass
                combined_word += word2[index]

        return combined_word