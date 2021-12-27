# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k<= 1 or head is None:
            return head
        dummy = ListNode(0, head)
        group_previous = dummy

        while True:
            kth = self.getKth(group_previous, k)
            if not kth:
                break
            group_next = kth.next

            previous = kth.next
            current = group_previous.next
            while current!=group_next:
                next_ = current.next
                current.next = previous

                previous = current
                current = next_

            temp = group_previous.next
            group_previous.next = kth
            group_previous = temp

        return dummy.next
            
        
    
    def getKth(self, current, k):
        while current and k>0:
            current = current.next
            k -= 1
        return current