# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        temp1 = even = ListNode()  # temp to track heads, cuz after iteration we need to 
        temp2 = odd = ListNode()   # connect these 2 list & we dont have track of heads
        
        curr_node = head
        i = 1
        while curr_node:
            if i % 2==0:
                even.next = curr_node
                even = even.next
            else:
                odd.next = curr_node
                odd = odd.next
            
            curr_node = curr_node.next
            i += 1
        
        
        even.next = None
        odd.next = None
        
        odd.next = temp1.next
        return temp2.next
            
        