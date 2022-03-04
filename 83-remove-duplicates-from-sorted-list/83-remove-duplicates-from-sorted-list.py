# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        
        prev_node = head
        curr_node = head.next
        
        while curr_node:
            if prev_node.val == curr_node.val:
                prev_node.next = curr_node.next
                curr_node = curr_node.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next
        return head
        