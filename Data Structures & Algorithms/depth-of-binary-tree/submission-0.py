# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # We recursively compute the maximum depth of the left and right subtrees.
        # At each recursive call, we add 1 to represent the current node’s level.
        # When we reach a null node (base case), we return 0.
        # As the recursive calls return (i.e., as we backtrack up the call stack),
        # we compare the depths of the left and right subtrees,
        # and propagate the larger one upward, building the final depth from bottom to top.

        # Time complexity: O(n)
        # Space complexity: O(n) ~ due to recursive call stack

        if root == None:
            return 0

        return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right))