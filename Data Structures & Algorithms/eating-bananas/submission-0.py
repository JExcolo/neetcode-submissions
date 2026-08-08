class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, e = 1, max(piles)
        k = e
        while s <= e:
            mid = (e + s) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            if time <= h:
                k = mid
                e = mid - 1
            else:
                s = mid + 1
        
        return k
        

            
        
