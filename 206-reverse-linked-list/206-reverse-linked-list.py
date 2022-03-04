# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        
        prev_node = None
        curr_node = head
        
        while curr_node:
            # save next node and link to previous node
            next_node = curr_node.next
            curr_node.next = prev_node
            
            # move ahead
            prev_node = curr_node
            curr_node = next_node
        return prev_node