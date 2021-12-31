# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        current = dummy
        while current.next and current.next.next: # atleast two nodes after dummy
            first = current.next
            second = current.next.next
            
            # (curr) dummy -> 1 -> 2 -> x            
            # reverse
            current.next = second
            first.next = second.next
            second.next = first
            
            # move to next pair
            current = current.next.next
        
        return dummy.next
            
            
        