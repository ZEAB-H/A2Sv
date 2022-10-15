 
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #store the total values in a variable
        total =sum(nums)
        
        leftSum=0
        
        for i in range(len(nums)):
            righSum= total-nums[i]-leftSum
            if leftSum==righSum:
                return i
            leftSum +=nums[i]
        return -1

 
            