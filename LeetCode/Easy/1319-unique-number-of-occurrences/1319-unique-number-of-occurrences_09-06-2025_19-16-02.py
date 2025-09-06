def compress_arr_by_occ(arr: list[int]) -> list[int]:
    compressed_dict = {}
    for i in arr:
        compressed_dict[i] = compressed_dict.get(i, 0) + 1
    return compressed_dict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        compressed_dict = compress_arr_by_occ(arr)
        if len(set(compressed_dict.values())) == len(compressed_dict):
            return True

        return False
