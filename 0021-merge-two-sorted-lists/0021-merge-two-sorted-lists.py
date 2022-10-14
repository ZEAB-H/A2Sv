# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        cur=ListNode(0)
        ans =cur
        
        while (a and b):
            if (a.val >b.val):
                cur.next=b
                b=b.next
            else:
                cur.next=a
                a=a.next
            cur=cur.next
        
        while(a):
            cur.next =a
            a=a.next
            cur=cur.next
                
        while(b):
            cur.next =b
            b=b.next
            cur=cur.next
            
        return ans.next
        