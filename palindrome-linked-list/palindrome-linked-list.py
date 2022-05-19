# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.getMid(head)
        second_half = self.reverse(mid)
        
        first_half = head
        
        while first_half and second_half:
            if first_half.val != second_half.val:
                return False
            
            first_half = first_half.next
            second_half = second_half.next
        return True
    
    def getMid(self,head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self,head):
        prev, curr = None, head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            
            prev = curr
            curr = next_node
        
        return prev
    
        