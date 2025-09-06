def str_to_occ_dict(word: str) -> dict:
    word_dict = {}
    for i in word:
        word_dict[i] = word_dict.get(i, 0) + 1
    return word_dict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_dict = str_to_occ_dict(word1)
        word2_dict = str_to_occ_dict(word2)
        
        if set(word1_dict) != set(word2_dict):
            return False
        
        if sorted(word1_dict.values()) != sorted(word2_dict.values()):
            return False
        
        return True