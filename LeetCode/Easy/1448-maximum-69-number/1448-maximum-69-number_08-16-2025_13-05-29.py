class Solution:
    def maximum69Number (self, num: int) -> int:
        changed = 0
        res = ""
        for i in str(num):
            if i == str(6) and changed == 0:
                changed = 1
                res = res + "9"
            else:
                res = res + str(i)

        return int(res)