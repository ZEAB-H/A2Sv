class Solution:
    def rotate(self, num: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """ 
        for i in range(0,k):
                num[:]=num[-i:] + num[:-i]



        """
    
        while k>=1:
                k-=1

                num.insert(0,num[-1])
                num.pop(-1)
        return num

    
