def isPalindrome(s: str) -> bool:
    length = len(s)
    return s[:length] == s[length::-1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #create a dict with alphanumeric as key and index as val
        s_dict = {}
        for key, val in enumerate(s):
            if s_dict.get(val):
                s_dict[val].append(key)
            else:
                s_dict.update({val: [key]})
        #remove all one element entry
        s_dict = {key: val for key, val in s_dict.items() if len(val) > 1}
        if len(s_dict) == 0:
            return s[0]
        #create dict by its range pair between first and last element
        n_dict = {}
        for key in s_dict:
            combination = list(itertools.combinations(s_dict[key], 2))
            for i in combination:
                temp_key = i[1] - i[0]
                temp_val = [i[0], i[1]]
                n_dict.setdefault(temp_key, []).append(temp_val)
        
        #sort dict by largest range
        n_dict = dict(sorted(n_dict.items(), reverse=True))
        for key in n_dict:
            for pair in n_dict[key]:
                if isPalindrome(s[pair[0]: pair[1] + 1]) == True:
                    return (s[pair[0]: pair[1] + 1])
        
        return s[0]