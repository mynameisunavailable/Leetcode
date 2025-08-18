class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        if len1 <= len2:
            minlen = len1
        else:
            minlen = len2

        result = ""
        for i in range(0, minlen):
            result += word1[i] + word2[i]
        
        if len1 < len2:
            result += word2[minlen:]
        elif len2 < len1:
            result += word1[minlen:]
        
        return result
