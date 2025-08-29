class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[j] >= k:
                j -= 1
                continue
            temp = nums[j] + nums[i]
            if temp == k:
                count += 1
                j -= 1
                i += 1
            elif temp > k:
                j -= 1
            else:
                i += 1
            
        return count