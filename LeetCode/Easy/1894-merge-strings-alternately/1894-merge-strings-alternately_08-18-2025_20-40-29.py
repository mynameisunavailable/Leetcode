class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        if len1 <= len2:
            minlen = len1
        else:
            minlen = len2

        result = []
        for i in range(minlen):
            result.append(word1[i])
            result.append(word2[i])
        result_str = "".join(result)
        
        if len1 < len2:
            result_str += word2[minlen:]
        elif len2 < len1:
            result_str += word1[minlen:]
        
        return result_str
