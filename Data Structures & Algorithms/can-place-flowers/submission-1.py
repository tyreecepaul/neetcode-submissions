class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    cnt += 1
                    flowerbed[i] = 1

        if cnt >= n:
            return True
        return False