class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        small = piles[:len(piles)//3]
        large = piles[len(piles)//3:]
        out = 0        
        for i in range(len(small)):
            out += large[2*i]
        
        return out