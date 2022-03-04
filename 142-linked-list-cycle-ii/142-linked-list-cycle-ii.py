# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast  = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow= slow.next         
            
            if slow==fast: # cycle found
                break
        else:
             return None # else clause with loop, exec when loop runs successfuly
        
        # mark slow to head and again move pointers
        # since fast is k nodes ahead of slow that means fast has 
        # already completed one loop in cycle when they meet 
        # their next meeting point will be start of cycle
        slow = head
        while slow != fast:
            slow= slow.next
            fast = fast.next
        return slow
            
        
        