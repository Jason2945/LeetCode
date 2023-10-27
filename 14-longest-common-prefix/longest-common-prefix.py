class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestCommonPre = ""
        shortestWord = min(strs, key=len)
        for index in range(len(shortestWord)):
            letter = shortestWord[index]
            for words in strs:
                if words[index] != letter:
                    return longestCommonPre
            longestCommonPre += letter
        return longestCommonPre

        