def isVowel(c: str) -> bool:
    vowel = "aeiou" #only lowercase
    vowelset = set(vowel)
    if c in vowelset:
        return True
    return False

def maxSubs(n_list: list, k: int) -> int:
    #initialise substring vowel val
    subs = n_list[:k]
    temp_val = 0
    for i in subs:    
        temp_val += i
    
    #count max subs
    length = len(n_list)
    l = 0
    r = k
    max_val = temp_val
    while r < length:
        temp_val = temp_val - n_list[l] + n_list[r]
        if temp_val > max_val:
            max_val = temp_val
        l += 1
        r += 1
    
    return max_val

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k > len(s):
            return (-1)

        v_list = [1 if isVowel(i) == True else 0 for i in s]
        max_vowel = maxSubs(v_list, k)

        return max_vowel
