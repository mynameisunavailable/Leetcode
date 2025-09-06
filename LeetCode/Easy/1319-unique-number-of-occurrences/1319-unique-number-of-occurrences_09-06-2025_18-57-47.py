def compress_arr_by_occ(arr: list[int]) -> list[int]:
    previous = arr[0]
    count = 0
    compressed_arr = []
    for i in arr:
        if i == previous:
            count += 1
        else:
            compressed_arr.append(count)
            count = 1
            previous = i
    compressed_arr.append(count)
    
    return compressed_arr

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        compressed_arr = compress_arr_by_occ(arr)
        compressed_arr_set = set(compressed_arr)
        if len(compressed_arr) == len(compressed_arr_set):
            return True

        return False