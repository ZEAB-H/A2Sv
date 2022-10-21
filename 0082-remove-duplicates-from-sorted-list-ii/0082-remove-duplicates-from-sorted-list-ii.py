# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr={}
        temp=head
        
        while (temp!=None):
            if temp.val in arr:
                arr[temp.val]+=1
            else:
                arr[temp.val]=1
            temp=temp.next
        #filter the duplicates
        no_duplicates=[i for i in arr if arr[i]==1]
        
        #reconstruct the linked list
        if len(no_duplicates) == 0:
            return None
        new_head = ListNode(val=no_duplicates[0])
        new_curr = new_head
        for i in no_duplicates[1:]:
            new_curr.next = ListNode(val=i)
            new_curr = new_curr.next
        
        return new_head