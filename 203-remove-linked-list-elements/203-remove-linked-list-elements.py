# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        prev_node = None
        curr_node = head
        
        while curr_node:
            
            # delete the node
            if curr_node.val == val:
                if curr_node == head:
                    head = curr_node = curr_node.next # v.imp
                
                else:
                    prev_node.next = curr_node.next
                    curr_node = curr_node.next
            
            else: # move ahead
                prev_node = curr_node
                curr_node = curr_node.next
        
        return head
                
                    
                    
        
            
        
        
        