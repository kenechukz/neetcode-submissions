# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Example 1:
    2^2 x 1 +2^0 x 1 = 4 + 1 = 5 
    Method:
    - Get length of linked list using length
    - Carry out operation on each node: 2^y x z, where y is the length minus 1, and z is either a 1 or 0
    - Subtract 1 from y each time
    - Add result of each operation to a variable called base10
    """

    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        base10 = 0
        length = 0

        # Get length of linked list using length
        while curr != None:
            length+=1
            curr = curr.next

        # reseting current
        curr = head

        # carry out operation on each node: 2^y x z, where y is the length minus 1, and z is either a 1 or 0
        y = length-1
        while curr != None:
            base10 += (2**y) * curr.val
            y-= 1
            curr = curr.next

        return base10

