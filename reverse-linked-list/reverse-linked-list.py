# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        previous,current = None,head
        while current:
            next_ = current.next
            current.next = previous
            
            previous = current
            current = next_
        return previous
        