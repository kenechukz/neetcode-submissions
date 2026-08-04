# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# recursion
# 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited = set()
        cur = head


        while cur != None:

            if cur in visited:
                return True
            else:
                visited.add(cur)
            cur = cur.next

        return False

        

        