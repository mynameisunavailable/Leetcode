class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove all non alphanumeric
        #convert upper to lower
        s_list = [x.lower() for x in s if x.isalnum() == True]
        # print(s_list)
        
        #reverse list and compare with s_list
        return s_list == s_list[::-1]