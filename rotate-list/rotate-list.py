# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:     
        if k<=0 or not head:
            return head
        
        current,length = head, 1
        while current.next:     
            current = current.next
            length += 1
        
        tail = current
        k = k % length # if k is oob
        if k==0:
            return head
        
        current = head
        for _ in range(length-k-1):
            current = current.next
        
        new_head=  current.next
        current.next = None # break chain
        
        tail.next = head
        return new_head
        
                
            
        
        
    
        
        