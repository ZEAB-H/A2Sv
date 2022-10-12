class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        n=len(tree)
        counter= defaultdict(int)
        
        left=0
        ans=0
        for right, f in enumerate(tree):
            counter[f] +=1
            
            while   len(counter)>2:
                counter[tree[left]] -=1
                if counter[tree[left]]==0:
                    del counter[tree[left]]
                left +=1
            
            ans =max(ans, right-left+1)
        
        return ans