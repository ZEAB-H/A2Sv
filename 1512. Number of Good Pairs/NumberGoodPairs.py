class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs= 0
        d={}
        for num in nums:
            if num not in d :
                d[num]=1
            else:
                d[num] +=1
                good_pairs += d[num]-1
            
        return good_pairs
  
                
   