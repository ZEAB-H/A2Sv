class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N =len(nums)
        INF = 10 ** 20
        
        
        dp = [-INF] * N
        dp[0]= nums[0]
        q= collections.deque()
        q.append(dp[0])
        
        
        for i in range(1,N):
            best= -INF
            
            best= q[0]
            dp[i]= best + nums[i]
            
            
            while len(q)> 0 and q[-1]<dp[i]:
                q.pop()
                
            q.append(dp[i])
            if i>=k :
                if len(q)>0 and q[0] == dp[i-k]:
                    q.popleft()
                    
        return  dp[N-1]
        
        