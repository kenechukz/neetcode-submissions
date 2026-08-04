# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 -> 5
        # prev = null
        # on each iteration
        # next = curr.next
        # curr.next = prev
        # prev = curr
        # curr = next

        # first pass
        # next = 2
        # null<-1
        # prev = 1
        # curr = 2

        # next = 3
        # null <- 1 <- 2
        # prev = 2
        # curr = 3

        # .....
        # execute until curr == null

        # Edge cases
        # if head is null or size is 1 return head

        # Time complexity: O(n)
        # Space complexity: O(1)

        if head == None or head.next == None:
            return head
        cur = head
        prev = None
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

        return prev


        




        