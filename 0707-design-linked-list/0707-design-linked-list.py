class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        

    def get(self, index: int) -> int:
        if index<0 or index>1000 or not self.head:
            return -1
        
        N = self.head
        for i in range(0,index):
           if (N.next==None):
               return -1
           N= N.next
            
        return N.val
              
        

    def addAtHead(self, val: int) -> None:
        N= Node(val)
        N.next=self. head
        self.head=N
        
        
        

    def addAtTail(self, val: int) -> None:
        t=Node(val)
        if self.head:
            curr=self.head
            while curr.next:
                curr = curr.next 
            curr.next = t
        else:
            self.addAtHead(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index ==0:
            self.addAtHead(val)
        elif self.head :
            i=0
            prev=None
            Curr=self.head
            while Curr.next and i !=index :
                i +=1
                prev =Curr 
                Curr=Curr.next 
            if index == i:
               newN= Node(val)
               prev.next =newN
               newN.next=Curr 
            elif index == i +1:
               Curr.next=Node(val)
        

    def deleteAtIndex(self, index: int) -> None:
        if  self.head:
            i = 0
            prevNode = None
            currentNode = self.head
            while currentNode.next and i != index :
                i += 1
                prevNode = currentNode
                currentNode = currentNode.next

            if i == index: 
                if i == 0:
                    self.head = currentNode.next
                else :
                    prevNode.next = currentNode.next
                del currentNode


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)