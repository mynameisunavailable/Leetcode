class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        back = len(s) - 1
        s = list(s)
        i = 0
        while i < back:
            if s[i] in vowels:
                while s[back] not in vowels:
                    back -= 1
                s[i], s[back] = s[back], s[i]
                back -= 1
            i += 1
        return "".join(s)