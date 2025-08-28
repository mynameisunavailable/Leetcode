class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_dict = {}
        templen = maxlen = last = 0
        i = j = 0
        while i + maxlen < len(s):
            if s_dict.get(s[i + j], -1) >= i: #found value in dict higher than left
                last = s_dict[s[i + j]]
                s_dict[s[i + j]] = i + j
                templen = templen - last + i
                i = last + 1
                j = templen
            else: #add value in dict
                s_dict[s[i + j]] = i + j
                templen += 1
                j += 1
            maxlen = max(maxlen, templen)

        return (maxlen)