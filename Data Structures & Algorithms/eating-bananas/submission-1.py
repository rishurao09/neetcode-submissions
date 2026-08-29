class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l  = 1 
        r = max(piles)
        while l <= r :
            mid = (l+r) // 2
            speed = 0
            for i in piles : 
                speed += math.ceil(i/mid) 
            if speed <= h :
                r = mid-1
            else : 
                l = mid + 1 
        return l
            