class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxval = 0
        curval = 0
        for i in gain:
            curval += i
            maxval = max(curval, maxval)
        
        return maxval