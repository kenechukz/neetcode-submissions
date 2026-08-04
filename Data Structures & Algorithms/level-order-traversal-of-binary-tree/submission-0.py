# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = []
        res = []
        if root is None:  # Handle the case where the tree is empty
            return res

        queue.append(root)
        while queue:
            curLen = len(queue)
            curLvl = []
            while curLen > 0:    
                cur = queue.pop(0)
                
                if cur == None:
                    continue

                curLvl.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

                curLen -= 1

            res.append(curLvl)
            
        return res

            



        