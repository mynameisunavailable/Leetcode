class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(" ")
        s = [x for x in s if x != ""]
        result = []
        for i in reversed(range(0, len(s))):
            result.append(s[i])
            
        return " ".join(result)