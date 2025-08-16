def split_by_dup(s: str):
    seen = set()
    for key, val in enumerate(s):
        if val in seen:
            return s[: key]
        seen.add(val)
    return len(s)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        temp_len = 0
        max_len = 0
        s_len = len(s)
        for i in s:
            if s_len - count < max_len:
                return max_len
            temp_str = split_by_dup(s[count:])
            if type (temp_str) == int:
                if temp_str > max_len:
                    return temp_str
                else:
                    return max_len
            if type(split_by_dup(temp_str)) == str:
                temp_len = self.lengthOfLongestSubstring(temp_str)
            else:
                temp_len = split_by_dup(temp_str)
            if temp_len > max_len:
                max_len = temp_len
            count += 1
        return (max_len)