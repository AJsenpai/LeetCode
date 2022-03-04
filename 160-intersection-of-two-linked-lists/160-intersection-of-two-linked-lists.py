# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        - if both lists are of equal length then we simply move two
          pointers until the p1 and p2 has equal values
        
        - if the lenght is uneven then as soon as one pointer reaches the tail
          we make it the head of another pointer 
          
          if p1.next is None:
            make p1 head of p2
            p1 = p2head
        
        - in this way at some point both pointers will be in sync before they reach
          end 
        '''
        a = headA
        b = headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a