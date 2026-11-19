# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def bfs(root):
            result = []
            queue = []
            queue.append(root)

            while queue:
                current = queue.pop(0)

                if current == None:
                    result.append(None)
                    continue
                result.append(current.val)

                

                if current.left:
                    queue.append(current.left)
                
                if current.right and not current.left:
                    queue.append(None)
                    queue.append(current.right)
                elif current.right:
                    queue.append(current.right)

                

            

            return result


    


        return bfs(p) == bfs(q)

        