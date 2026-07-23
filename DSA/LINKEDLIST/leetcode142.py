# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        hascycle= False
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                hascycle = True
                break
        if not hascycle:
            return None    
        l=0
        while slow.next!=fast:
            slow=slow.next
            l+=1
        l+=1
        slow=slow.next
        slow=head
        fast=head
        for i in range(l):
            fast=fast.next
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow                    
