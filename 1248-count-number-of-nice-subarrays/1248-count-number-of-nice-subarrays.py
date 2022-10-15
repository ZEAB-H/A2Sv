class Solution:
    def numberOfSubarrays(self, A: List[int], k: int) -> int:
        def f(k):
            res=i=j=    countOdd=0
            
            while j<len(A):
                countOdd += A[j] %2
                while countOdd >k:
                    countOdd -= A[i]%2
                    i +=1
                res +=j-i+1
                j +=1
            return res
        return f(k) -f(k-1)