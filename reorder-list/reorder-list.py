# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        first_half = head
        mid = self.findMid(head)        
        second_half = self.reverse(mid)
        
        while first_half and second_half:
            temp = first_half.next
            first_half.next = second_half
            first_half = temp
            
            temp = second_half.next
            second_half.next = first_half
            second_half = temp
        
        if first_half:
            first_half.next = None
            
        return head
    
    def reverse(self, head):
        previous,current = None, head
        while current:
            next_ = current.next
            current.next=  previous
            
            previous = current
            current = next_
        return previous
    
    def findMid(self, head):
        slow= fast = head        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next            
        mid = slow.next
        slow.next = None
        return mid