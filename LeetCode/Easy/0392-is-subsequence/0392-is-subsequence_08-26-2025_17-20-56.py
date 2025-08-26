class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        i = 0
        while i < len(t):
            if count > len(s) - 1:
                return True
            if t[i] == s[count]:
                count += 1
            i += 1
        
        return count == len(s)