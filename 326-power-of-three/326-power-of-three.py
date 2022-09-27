class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(10):
            print(bin(3**i))
            
        
        while n>1 and n%3 ==0:
            n//=3
        return n==1
         