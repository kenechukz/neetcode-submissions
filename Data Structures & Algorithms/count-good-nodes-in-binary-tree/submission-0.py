# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    numGoodNodes = 0
    def goodNodes(self, root: TreeNode) -> int:


        # root always good node
        # to solve sub problem: check if parent node val > child node val
        # edge case root has no children
        
        # I used a recursive approach to count all "good" nodes in a binary tree.
        # A node is considered "good" if its value is greater than or equal to all values
        # along the path from the root to that node.
        # First, I check if the root has no children — if so, it's a single good node, so I return 1.
        # I solve the problem recursively by checking each child node: if the node's value is greater than
        # or equal to the max value seen so far in the path, I count it as a good node.
        # To do this, I keep track of the max value from the root down to the current node.
        # This way, each node compares its value not just to its direct parent,
        # but to the maximum value found along the path to it.

        # Time complexity: O(N) ~ where N is the total number of nodes — each node is visited once.
        # Space complexity: O(H) ~ where H is the height of the tree (due to the recursion stack).



        if not root.left and not root.right:
            return 1 

        maxParent = -100000

        def recursion(parent, root, maxParent):
            
            if root == None:
                return self.numGoodNodes

            if root.val >= maxParent:
                self.numGoodNodes += 1
                maxParent = root.val

            recursion(root, root.left, maxParent)
            recursion(root, root.right, maxParent) 
            return self.numGoodNodes


        return recursion(None, root, maxParent)










        