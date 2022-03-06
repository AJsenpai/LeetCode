# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        curr_node = dummy # prev_node
        
        while curr_node.next and curr_node.next.next:
            
            first = curr_node.next
            second = curr_node.next.next
            
            
            
            # swap
            curr_node.next = second # prev node points to second
            first.next= second.next
            second.next = first
            
            
            curr_node = curr_node.next.next
        
        return dummy.next
            
            
            
            
        