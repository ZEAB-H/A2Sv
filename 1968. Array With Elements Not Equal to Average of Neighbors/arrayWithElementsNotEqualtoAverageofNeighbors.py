class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        left=0
        right=len(nums)-1
        result=[]
        while left<=right:
            if left!=right:
                result.append(nums[right])
                result.append(nums[left])
            else:
                result.append(nums[left])
                 
            right=right-1
            left=left+1
        return result    
      