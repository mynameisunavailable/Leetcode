class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_set, t_set = set(s), set(t)
        if s_set.issubset(t_set) == False:
            return False
        elif len(s) == 0:
            return True
        elif len(t) == 0:
            return False

        count = 0
        for i in t:
            if i == s[count]:
                count += 1
            if count > len(s) - 1:
                return True
        
        return False

