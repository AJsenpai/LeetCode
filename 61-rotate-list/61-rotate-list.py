# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k<0 or not head:
            return 
        
        curr_node = head
        length = 1
        
        while curr_node.next:
            curr_node = curr_node.next
            length+=1
        
        tail = curr_node
        k = k % length  # if k is larger number circle around
        
        if k==0: # rotate by zero
            return head
        
        curr_node = head
        # find the pivot node from where the rotation starts
        for _ in range(length-k-1):
            curr_node = curr_node.next
        
        
        # curr_node is pivot and new head is pivot.next, break the chain here
        new_head = curr_node.next         
        curr_node.next = None
        
        tail.next = head # link the chain again
        
        return new_head
        
        
        
        
        
        