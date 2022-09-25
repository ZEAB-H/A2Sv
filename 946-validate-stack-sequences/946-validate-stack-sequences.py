class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N =len(pushed)
        
        stack =[]
        index= 0
        
        for item in pushed:
            stack.append(item)
            
            while len(stack)>0 and index< N and popped[index]==stack[-1]:
                stack.pop()
                index +=1
        return index == N
        