class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove all non alphanumeric
        s_list = [x for x in s if x.isalnum() == True]
        # print(s_list)
        #convert upper to lower
        s_list = [x.lower() for x in s_list]
        # print(s_list)
        
        #reverse list and compare with s_list
        return s_list == s_list[::-1]
        # print(r_list)

        #check if front and back is equal
        # return true or false
        # if r_list == s_list:
        #     return True
        # else:
        #     return False
