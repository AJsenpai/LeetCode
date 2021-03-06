# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n<1 or not head:
            return 
        
        slow = fast = head
        
        # move fast pointer ahead n time        
        for _ in range(n):
            fast = fast.next
            
        # edge case - if fast is None -- head
        if fast is None:
            head = head.next
            return head
        
        while fast and fast.next:
            slow = slow.next
            fast =fast.next
        
        slow.next = slow.next.next
        
        return head
            
        
        
        