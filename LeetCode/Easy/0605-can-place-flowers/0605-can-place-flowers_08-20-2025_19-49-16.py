def add_10_to_right_if_blocked(flowerbed: list[int]):
    leng = len(flowerbed)
    blocked = 0
    for i in range(0, leng):
        if blocked == 1:
            flowerbed[i] += 10
            blocked = 0
        if flowerbed[i] % 10 == 1:
            blocked = 1
        else:
            blocked = 0

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        add_10_to_right_if_blocked(flowerbed)
        # print(flowerbed)
        flowerbed = list(reversed(flowerbed))
        add_10_to_right_if_blocked(flowerbed)
        # print(flowerbed)
        
        leng = len(flowerbed)
        blocked = 0
        for i in range(0, leng):
            if flowerbed[i] == 0 and n > 0:
                flowerbed[i] += 1
                n -= 1
                if i >= leng - 1:
                    break;
                flowerbed[i+1] += 10

        if n <= 0:
            return True
        else:
            return False