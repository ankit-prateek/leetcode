class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        #calculate the length of the linked list
        n = 0
        ptr = head
        while ptr:
            n += 1
            ptr = ptr.next
            
        node_end = n - k
        right = head
        while node_end > 0:
            node_end -= 1
            right = right.next
            
        left = head
        while k > 1:
            k -= 1
            left = left.next
            
        tmp = right.val
        right.val = left.val
        left.val = tmp
        
        return head