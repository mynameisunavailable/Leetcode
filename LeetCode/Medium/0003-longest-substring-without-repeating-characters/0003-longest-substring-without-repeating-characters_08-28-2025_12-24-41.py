class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_dict = {}
        templen = maxlen = 0
        i = j = 0
        while i + maxlen < len(s):
            if s_dict.get(s[i + j], -1) != -1: #found value in dict
                templen -= 1
                s_dict.pop(s[i])
                i += 1
                j -= 1
            else: #add value in dict
                s_dict[s[i + j]] = i + j
                templen += 1
                j += 1
            maxlen = max(maxlen, templen)

        return (maxlen)
