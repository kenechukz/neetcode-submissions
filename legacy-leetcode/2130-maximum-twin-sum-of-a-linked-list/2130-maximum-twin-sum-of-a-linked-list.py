# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # prerequisites
        # length ALWAYS even
        # min length in 2
        # twin sum =  node i + node n-1-i

        # 5 -> 2 -> 4 -> 1 -> 3 -> 2
        # 0    1    2    2 twin 1 twin 0 twin
        # node
        # twin
        # output return max twin sum
        # base case when len is 2

        # First I found middle node using fast slow pointers, slow will be middle node
        # From the slow pointer I began to reverse the twin half of linked list
        # At the end I let twinHead point to prev which is node before cur when it becomes null i.e. head of reversed list
        # Finally I started current node (cur) at head and calculated each twin sum by adding current node's value 
        # and twinHead's value together, comparing twinSum to max twinSum value and setting max accordingly
        # I then changed cur and twinHead to point to next nodes.

        
        # Time Complexity: O(n)
        # Space Complexity: O(1) ~ Partial list reversal is done in place

        if head.next.next == None:
            return head.val + head.next.val

        fast = slow = head
        # find middle
        while fast:
            slow = slow.next
            fast = fast.next.next

        # slow is at middle node
        cur = slow
        prev = None
        while cur:
            # reverse twin part of linked list
            forward = cur.next
            cur.next = prev
            prev = cur
            cur = forward
        twinHead = prev
        
        # Checking max sum
        maxSum = 0
        cur = head
        while cur != slow:
            twinSum = cur.val + twinHead.val
            if twinSum > maxSum:
                maxSum = twinSum
            cur = cur.next
            twinHead = twinHead.next

        return maxSum
            








        
                


           

           







        
            
            

        
         


        