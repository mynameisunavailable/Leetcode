class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        count = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[j] <= k:
                if nums[j] + nums[i] == k:
                    count += 1
                    j -= 1
                    i += 1
                elif nums[j] + nums[i] > k:
                    j -= 1
                elif nums[j] + nums[i] < k:
                    i += 1
            else:
                j -= 1
            
        return count