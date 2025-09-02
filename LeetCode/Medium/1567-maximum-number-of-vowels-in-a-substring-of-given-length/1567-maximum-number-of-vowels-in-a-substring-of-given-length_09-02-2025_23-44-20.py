class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k > len(s):
            return (-1)

        vowels = set("aeiou")
        #initialise substring vowel val
        subs = s[:k]
        temp_val = 0
        for i in subs:
            if i in vowels: 
                temp_val += 1
        
        #count max subs
        length = len(s)
        l = 0
        r = k
        max_val = temp_val
        while r < length:
            if s[l] in vowels:
                temp_val = temp_val - 1
            if s[r] in vowels:
                temp_val = temp_val + 1
            if temp_val > max_val:
                max_val = temp_val
            l += 1
            r += 1
        
        return max_val