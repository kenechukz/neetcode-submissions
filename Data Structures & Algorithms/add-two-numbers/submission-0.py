# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        """
        342             243
        465             564
        807             708


        add two linked lists and store in same reversed order

        E:
        [1, 100]
        0 <= Node.val <= 9

        No leading 0s

        A:
        I could take values of each linked list
        make them num1 and num2, add the result then make 
        a linked list to store the result

        ^^^
        O(n) solution


        243
        564 c=1
        708

        """


        bigger = -1

        cur = l1
        l1Size = l2Size = 0
        while cur:
            cur = cur.next
            l1Size +=1 

        cur = l2
        while cur:
            cur = cur.next
            l2Size +=1 

        if l2Size >= l1Size:
            bigger = l2
            smaller = l1
        else:
            bigger = l1
            smaller = l2

        c = 0
        resHead = ListNode(-1)
        resHead.next = bigger
        while bigger and smaller:
            newDigit = (bigger.val + smaller.val) + c
            bigger.val = newDigit % 10
            c = newDigit // 10
            prev = bigger
            bigger = bigger.next
            smaller = smaller.next

        while bigger and c > 0:
            total = bigger.val + c
            bigger.val = total % 10
            c = total // 10
            prev = bigger
            bigger = bigger.next

        if c > 0:
            prev.next = ListNode(c)

        return resHead.next

        """
        01111
        9999999 
        9999
        8999000
        """



