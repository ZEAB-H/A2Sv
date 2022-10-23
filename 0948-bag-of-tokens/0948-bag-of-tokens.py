class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        N=len(tokens)
        
        
        best=0
        score=0
        p=power
        
        left=0
        right=N-1
        
        while left<=right:
            if p >= tokens[left]:
                p -=tokens[left]
                score +=1
                left +=1
                best =max(best,score)
            else:
                if score>0:
                    p+=tokens[right]
                    score-=1
                    right-=1
                else:
                    break
        return best