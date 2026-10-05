# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Method:
# Find length of list
# Delete nodes below start index


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0
        startIdx = 0
        count = 0

        # Find length of List
        while curr != None:
            length+=1
            curr = curr.next

        if length % 2 == 0:
            startIdx = length / 2
        else:
            startIdx = floor(length / 2)

        # reseting current
        curr = head

        while curr != None: 
            if count < startIdx:
                head = curr.next
            else:
                return head
                
            count += 1
            curr = curr.next
            

        
        







