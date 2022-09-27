class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(10):
            print(bin(4**i))
            
        
        while n>1 and n%4 ==0:
            n//=4
        return n==1