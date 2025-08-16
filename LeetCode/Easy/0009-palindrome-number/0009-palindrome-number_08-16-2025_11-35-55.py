import math

def len_int(x):
    if x < 0:
        x = -x
    elif x == 0:
        return 1
    else:
        return int(math.log10(x)) + 1
        
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        len_x = len_int(x)
        last_half = 0
        i = 0
        while i < (len_x / 2):
            last_half = (last_half * 10) + (x % 10)
            x //= 10
            i += 1
        if len_int(x) - 1 == len_x / 2:
            x //= 10
        if x - last_half == 0:
            return True
        return False