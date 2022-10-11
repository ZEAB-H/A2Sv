class Solution:
    def moveZeroes(self, num: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        for this probs we will try to solve it by using the two pointers named original and modified ,         and use them to move the zeros to the end
        '''
        
        original=0
        modified=0
        
        for original in range(0,len(num)):
            if num[original]:   # checking if the element of the array is different from 0
                num[modified]=num[original] 
                modified+=1
            original+=1
         
        while modified < len(num):
            num[modified]=0
            modified+=1
        