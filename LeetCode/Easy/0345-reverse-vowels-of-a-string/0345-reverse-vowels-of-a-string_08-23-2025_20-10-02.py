class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        back = len(s) - 1
        s = list(s)
        for i in range(0, len(s)):
            if s[i] in vowels:
                while s[back] not in vowels:
                    back -= 1
                s[i], s[back] = s[back], s[i]
                back -= 1
            if i >= back:
                break
        return "".join(s)