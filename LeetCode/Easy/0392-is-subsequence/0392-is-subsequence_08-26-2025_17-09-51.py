class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False

        count = 0
        i = 0
        while i < len(t):
            if t[i] == s[count]:
                count += 1
            if count > len(s) - 1:
                return True
            i += 1
        
        return False