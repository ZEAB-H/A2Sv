class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
         freq = collections.Counter(nums)
            
         pairs =0
        
         for key in freq.keys():
             a, b = key , k-key
             if a<b:
                 pairs += min(freq[a], freq[b])
             elif a == b:
                 pairs += freq[a] //2
                
         return pairs
    