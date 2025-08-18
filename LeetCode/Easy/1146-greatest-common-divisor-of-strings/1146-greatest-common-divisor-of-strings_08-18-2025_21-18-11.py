def isdivisible(string: str, divisor: str) -> bool:
    temp = string.split(divisor)
    #remove empty str
    temp = [x for x in temp if x != ""]
    if temp == []:
        return True
    else:
        return False

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        if len1 <= len2:
            minlen = len1
        else:
            minlen = len2

        for i in reversed(range(minlen)):
            divisor = str2[: i + 1]
            if isdivisible(str1, divisor) and isdivisible(str2, divisor):
                return divisor
        return ""