class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find shortest str len
        min_len = len(strs[0])
        c_pre = strs[0]
        for str in strs:
            temp_len = len(str)
            if temp_len < min_len:
                min_len = temp_len

        #search the first letter of each word, then second etc
        i, j = 0, 0
        list_len = len(strs)
        if list_len == 1:
            return strs[0]

        for char in strs[0]:
            # print(char)
            i = 0
            for count in range(0, list_len):
                # print(i, j)
                if char != strs[i][j] or j >= min_len:
                    # print("difference found!")
                    c_pre = strs[i][0:j]
                    return c_pre
                i += 1
            j += 1
            
        return c_pre