class Solution:
    def sortSentence(self, s: str) -> str:
        final=[""]*10
        
        current=0
        
        temp= ""
        
        while current<len(s):
            if s[current]==" ":
                current +=1
            try:
                index=int(s[current])
                final[index]=temp
                current +=1
                temp= ""
            except:
                temp += s[current]
                current +=1
               
        string =""
        
        for word in final:
            if len(word)== 0:
                continue
            if len(string)==0:
                string = word
            else :
                string +=" " + word 
        
        
        return string
            
              
