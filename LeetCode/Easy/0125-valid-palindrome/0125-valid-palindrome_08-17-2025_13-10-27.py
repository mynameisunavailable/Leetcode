class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [x.lower() for x in s if x.isalnum()]
        return s_list == s_list[::-1]