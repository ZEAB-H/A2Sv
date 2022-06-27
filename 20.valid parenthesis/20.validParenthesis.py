class Solution:
    def isValid(self, s: str) -> bool:
        # create pairs, if pair is in string, then take it out
        # if cannot take anymore out then end w false
        
        pairs = ["{}", "[]", "()"]
        
        while any([pair in s for pair in pairs]):
            for pair in pairs:  
                s = s.replace(pair,"")
    
    
        return len(s)==0