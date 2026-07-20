# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        curr=head
        l=0
        while curr!=None:
            curr=curr.next
            l+=1
        curr=head
        for i in range((l//2)-1):
            curr=curr.next
        curr.next=curr.next.next
        return head    
