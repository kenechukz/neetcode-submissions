# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


        # a node is a leaf if it has no children
        # Time complexity: O(n)
        # Space complexity: O(n)

        leaves1 = []
        leaves2 = []

        def findLeaves(root, leaves):

            if root == None:
                return leaves

            if root.left == None and root.right == None:
                leaves.append(root.val)
                return leaves

            findLeaves(root.left, leaves)
            findLeaves(root.right, leaves)

            return leaves

        return findLeaves(root1, leaves1) == findLeaves(root2, leaves2)
        

                 

            


        