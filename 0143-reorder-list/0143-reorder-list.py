# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        temp=head
        i=0
        while temp!=None:
            if i%2==0:
                temp.val=arr.pop(0)
            else:
                temp.val=arr.pop()
            temp=temp.next
            i+=1
                       
       