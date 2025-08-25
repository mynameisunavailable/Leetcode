class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        n1 = nums[0]
        n2 = None
        for i in range(len(nums)):
            if nums[i] <= n1:
                n1 = nums[i]
            elif n2 is None or nums[i] <= n2:
                n2 = nums[i]
            else:
                return True

        return False
