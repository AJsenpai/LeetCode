# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], p: int, q: int) -> Optional[ListNode]:        
        if p==q:
            return head
        
        # 1 - 2 - 3 - 4 - 5  
        # p = 1, q = 3
        
        prev_node = None
        curr_node = head
        
        i=0
        while curr_node and i < p-1:
            prev_node = curr_node
            curr_node = curr_node.next
            i +=1
        
        last_node_of_previous = prev_node # 1
        last_node_of_sublist = curr_node  # 2
        
        # 3 parts, node before p, sublist, node after q
        
        next_node = None
        i = 0 
        while curr_node and i < q-p+1:
            next_node = curr_node.next
            curr_node.next = prev_node
            
            prev_node = curr_node
            curr_node = next_node
            
            i+=1
        
        # merge the reversed sublist with original chain
        if last_node_of_previous is not None:
            # prev is the head of reversed sublist
            last_node_of_previous.next = prev_node 
        else:
            head = prev_node
        
        last_node_of_sublist.next = curr_node # prev = 4, curr_node = 5
        
        return head
        
        
        
        
        
        
        
        
        
        
        