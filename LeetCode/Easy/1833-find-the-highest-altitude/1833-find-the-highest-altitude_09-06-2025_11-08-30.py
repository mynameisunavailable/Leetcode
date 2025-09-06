class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        length = len(gain)
        gain.append(0)
        total = 0
        for i in range(length):
            total = total + gain[i]
            gain[i] = total
        return max(gain)