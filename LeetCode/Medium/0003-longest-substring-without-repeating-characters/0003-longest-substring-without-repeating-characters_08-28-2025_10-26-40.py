class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        templen = maxlen = 0
        i = 0
        while i < len(s):
            while i + templen < len(s):
                if s[i + templen] in seen:
                    seen.remove(s[i])
                    templen -= 1
                    break    
                seen.add(s[i + templen])
                templen += 1
                maxlen = max(maxlen, templen)
            i += 1

        return (maxlen)