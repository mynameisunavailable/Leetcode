class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_dict = {}
        maxlen = last = 0
        i  = j = 0
        while i + maxlen < len(s): #early terminate if longer substring is not possible
            if s_dict.get(s[i + j], -1) >= i: #found value in dict higher than left
                last = s_dict[s[i + j]] #previous index for the item
                s_dict[s[i + j]] = i + j #update to new index
                j = j - last + i #new j is j - (diff between last index and left)
                i = last + 1 #move window to right by 1
            else: #add value in dict
                s_dict[s[i + j]] = i + j
                j += 1
            maxlen = max(maxlen, j)

        return (maxlen)
