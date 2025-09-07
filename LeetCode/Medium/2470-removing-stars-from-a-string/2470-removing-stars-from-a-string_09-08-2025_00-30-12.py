class Solution:
    def removeStars(self, s: str) -> str:
        s_list = []
        for i in s:
            if i == "*":
                if s_list:
                    s_list.pop(-1)
            else:
                s_list.append(i)
        return "".join(s_list)