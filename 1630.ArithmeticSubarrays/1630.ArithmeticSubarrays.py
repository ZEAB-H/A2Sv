class Solution:
    def isArithmetic(self,nums):
       
        cd = nums[1] - nums[0]
        i = 2
        while i < len(nums):
            if nums[i]- nums[i-1] != cd:
                return False
            i += 1
        return True
    
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        m = len(l)
        i = 0
        while i < m:
            left = l[i]
            right = r[i]
            tempArr = nums[left:right+1]
            tempArr.sort()
            if right - left + 1 >= 3:
                ans.append(self.isArithmetic(tempArr))
            else:
                ans.append(True)
            i += 1
        return ans