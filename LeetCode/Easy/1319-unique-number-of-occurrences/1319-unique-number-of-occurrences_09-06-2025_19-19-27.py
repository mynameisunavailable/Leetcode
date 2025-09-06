import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        if len(set(c.values())) == len(c):
            return True

        return False