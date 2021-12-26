# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = new = ListNode()
        carry = 0        
        while l1 or l2 or carry:            
            add = 0
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            add += carry
            new.next = ListNode(add%10)
            new = new.next
            carry = add//10
        return temp.next
