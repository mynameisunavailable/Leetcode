class Solution:
    def removeStars(self, s: str) -> str:
        s_list = []
        for i in s:
            if i == "*":
                s_list.pop()
            else:
                s_list.append(i)
        return "".join(s_list)