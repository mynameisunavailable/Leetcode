class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        back = len(s) - 1
        new_s = ""
        for i in range(0, len(s)):
            if s[i] in vowels:
                while s[back] not in vowels:
                    back -= 1
                new_s += s[back]
                back -= 1
            else:
                new_s += s[i]
        # print(new_s)
        return new_s