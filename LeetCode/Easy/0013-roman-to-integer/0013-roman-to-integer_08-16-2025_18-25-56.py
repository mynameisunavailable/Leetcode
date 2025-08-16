class Solution:
    def romanToInt(self, s: str) -> int:
        romantoint_dict = {
            "I" : "1",
            "V" : "5",
            "X" : "10",
            "L" : "50",
            "C" : "100",
            "D" : "500",
            "M" : "1000",
        }
        res = 0
        count = 0
        str_len = len(s)
        while count < str_len:
            n1 = int(romantoint_dict[s[count]])
            if count + 1 < str_len:
                n2 = int(romantoint_dict[s[count + 1]])
            else:
                n2 = 0
            
            if n1 < n2:
                res = res - n1
            else:
                res = res + n1
            
            count += 1

        return res