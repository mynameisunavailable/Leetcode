import collections
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #check if len is same
        if len(word1) != len(word2):
            return False
        
        word1_count = collections.Counter(word1)
        word2_count = collections.Counter(word2)
        #check if all letters in 1 exist in 2 and vice versa
        if word1_count.keys() != word2_count.keys():
            return False

        #check if shape same
        if sorted(word1_count.values()) != sorted(word2_count.values()):
            return False

        return True
        