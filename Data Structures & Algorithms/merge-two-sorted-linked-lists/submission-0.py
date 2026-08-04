# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        R:
        inpt: lst 1, lst 2 (both sorted)

        return head of new sorted ll

        E:
        constr.:empty lists and neg values
        either or our lists is empty -> return non empty list (or empty list if both empty)

        once either list points to null, add rest of other list to new list
        tie breaker -> pick node lst 1
        A:
        list1 = [1,2,4], list2 = [1,3,5]
                     l              r

        newList = head - (1) *--> (1) *--> (2) *--> (3) *--> (4) *--> (5)  

        """

        newList = ListNode(-1)
        cur = newList
        l = list1
        r = list2
        while l and r:
            
            if l.val <= r.val:
                cur.next = l
                l =l.next
            else:
                cur.next = r
                r = r.next

            cur = cur.next

        if not l:
            cur.next = r
        if not r:
            cur.next = l
        
        return newList.next



        

