class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestCommonPre = ""
        for index in range(len(min(strs, key=len))):
            letter = strs[0][index]
            for words in strs:
                if words[index] != letter:
                    return longestCommonPre
            longestCommonPre += letter
        return longestCommonPre

        