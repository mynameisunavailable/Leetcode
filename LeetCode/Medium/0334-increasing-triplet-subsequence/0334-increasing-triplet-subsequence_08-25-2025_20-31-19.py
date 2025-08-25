class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        n1 = nums[0]
        n2_assigned = False
        for i in range(1, len(nums)):
            if n2_assigned == False:
                if nums[i] > n1:
                    n2 = nums[i]
                    n2_assigned = True
                elif nums[i] < n1:
                    n1 = nums[i]
            else:
                if nums[i] > n2 and n1 < n2:
                    return True
                elif nums[i] <= n1:
                    n1 = nums[i]
                elif nums[i] < n2:
                    n2 = nums[i]

        return False