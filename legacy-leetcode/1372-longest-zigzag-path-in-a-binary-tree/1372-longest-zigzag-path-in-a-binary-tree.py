# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # I do a dfs to find the max path.
    # On each recursive call I keep track of the cur path length.
    # My base case will return once I hit a null node.
    # We set maxPath to max between maxPath and curPath.
    # On the recursive case, if our cur direction is one way, we continue 
    # with the current path length by going in opposite direction, continuing zig-zag.
    # We also call dfs going in same direction, breaking current zig zag and 
    # essentially resetting current path length as we start zig zag from new node.
    # At the end of the dfs call to the root.left and root.right, we return the max path.

    # Time Complexity: O(n) ~ each node visited once
    # Space Complexity: O(n) ~ recursive call stack 
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.maxPath = 0
        def dfs(root, curDir, curPath): 
            # base case:
            if not root:
                return

            # recursive case:
            self.maxPath = max(self.maxPath, curPath)
            if curDir == "l":
                dfs(root.right, "r", curPath +1)
                dfs(root.left, "l", 1)
            
            else:
                dfs(root.left, "l", curPath +1)
                dfs(root.right, "r", 1)


        dfs(root.left, "l", 1)
        dfs(root.right, "r", 1)
        return self.maxPath


        