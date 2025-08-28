class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        templen = maxlen = last = 0
        i = 0
        while i + maxlen < len(s):
            while i + maxlen < len(s):
                if s[i + templen] in seen:
                    # print(i, templen, s[i: i + templen], s[i + templen])
                    last = s[i: i + templen].index(s[i + templen]) + 1
                    seen -= set(s[i: i + last])
                    templen -= last
                    break
                seen.add(s[i + templen])
                templen += 1
                maxlen = max(maxlen, templen)
            i += last

        return (maxlen)