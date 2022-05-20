class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0 , len(nums) -1
        answer =[]
        while left< right:
            answer.append(nums[left] + nums[right])
            left +=1
            right -=1
            
        return max(answer)
        