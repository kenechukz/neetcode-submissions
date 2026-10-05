# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # midIdx = n // 2

        # first get size of ll

        # 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
        # size: 7
        # midIdx = 3

        # cur = 7
        # prev = midIdx-1
        # prev.next = cur.next
        # cur.next = null

        # 4 -> 1
        # 7 -> null

        # base case
        if not head.next:
            return head.next

        cur = head
        size = 0

        # get size of ll
        while cur:
            size += 1
            cur = cur.next

        midIdx = size // 2
        prev = midIdx - 1
        cur = head
        curIdx = 0

        while cur:

            if prev == curIdx:
                prev = cur
            
            elif midIdx == curIdx:
                prev.next = cur.next
                cur.next = None


            cur = cur.next
            curIdx+= 1
        
        return head

            




        