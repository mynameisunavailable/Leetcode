class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        result = list(s)[::-1]
        return " ".join(result)