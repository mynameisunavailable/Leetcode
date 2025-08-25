class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        n1 = nums[0]
        n2 = min(nums)
        n2_assigned = False
        for i in range(1, len(nums)):
            if nums[i] < n1:
                n1 = nums[i]
            elif n2 <= n1 and nums[i] > n1:
                n2 = nums[i]
                n2_assigned = True
            elif nums[i] < n2 and nums[i] > n1:
                n2 = nums[i]
            if nums[i] > n2 and n1 < n2 and n2_assigned == True:
                return True

        return False