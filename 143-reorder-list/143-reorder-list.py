# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        mid = self.getMid(head)
        second_half = self.reverse(mid)
        
        first_half = head
        
        while first_half and second_half:
            
            temp = first_half.next
            first_half.next = second_half
            first_half = temp
            
            temp = second_half.next
            second_half.next = first_half
            second_half = temp
        
        # if first_half: # already pointing to null, not needed
        #     first_half.next = None
        
        
    
    def getMid(self,head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next # store mid and break the chain
        slow.next = None
        return mid
    
    def reverse(self, head):
        prev_node = None
        curr_node = head
        
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            
            prev_node = curr_node
            curr_node = next_node
        
        return prev_node
        