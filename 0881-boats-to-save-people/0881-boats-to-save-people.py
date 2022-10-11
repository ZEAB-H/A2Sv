class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
         # we will try to sort the peoples first according to their weights and assign the boats for 
         # the lightest and  heaviest together 
         people.sort() 
         light= 0
         heaviest=len(people)-1
         numOfBoats= 0
            
         while light <= heaviest:
            numOfBoats +=1            
            if people[light] + people[heaviest] <= limit:
                light +=1
            heaviest -=1
            
         return numOfBoats
    


        
        
        
        
        
 

 
