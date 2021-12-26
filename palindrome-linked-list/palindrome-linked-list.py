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
            if first_half.val !=second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True

    def reverse(self,head):
        previous,current = None,head
        while current:
            next_ = current.next
            current.next = previous
            
            previous = current
            current = next_
        return previous
    
    def getMid(self,head):
        slow=fast= head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        