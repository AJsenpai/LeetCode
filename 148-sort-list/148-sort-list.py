# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if not head or not head.next:            
            return head
        
        # merge sort
        mid =  self.midPoint(head)
        
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left,right)
    
    def midPoint(self,head):
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(self,left,right):
        dummy = curr_node = ListNode()
        
        while left and right:
            
            if left.val < right.val:
                curr_node.next = left
                left = left.next            
            
            else:
                curr_node.next = right
                right = right.next
            
            curr_node = curr_node.next
        
        # remaining elements in any list
        curr_node.next = left or right
        
        return dummy.next
    
    