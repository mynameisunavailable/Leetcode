class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums)
        count = 0
        i = 0
        j = len(nums_sorted) - 1
        while i < j:
            if nums_sorted[j] + nums_sorted[i] == k:
                count += 1
                j -= 1
                i += 1
            elif nums_sorted[j] + nums_sorted[i] > k:
                j -= 1
            else:
                i += 1
            
        return count