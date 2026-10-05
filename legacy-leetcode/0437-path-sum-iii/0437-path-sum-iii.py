# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict 

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        # I go down the tree and check if there is a prefixSum key (prefixSum is a previous curSum) that 
        # is equal to the curSum - targetSum. If it exists its value will be greater 
        # than 0 and we will let that value equal count.
        # Key in prefixSum is the prefixSum value is count of the prefixSum,
        # i.e. increments everytime prefixSum has occured.
        # We then increment the the value of the curSum key in the prefix sum map
        # We add the result of the left and right subtree to count 
        # We then backtrack after adding the result of left and right subtree by decrementing value of curSum key
        # in the prefix sum map as that prefixSum will no longer be possible when we go up the tree
        # Finally we return the count, from recursive call to recursive call
        # For instance in example 1, from the root 10 
        # the count+= dfs(root.left, curSum) will add 2 and the count += dfs(root.right, curSum)
        # will add 1
        # Overall this adds 3 to count which is prefixSum[curSum - targetSum] for current root
        # prefixSum[10-8] = prefixSum[2] at that point has value 0
        # return count will yield 3

        # Time Complexity: O(N) ~ Number of nodes, which are each visisted once
        # Space Complexity: O(N) ~ O(H) for recursion, The depth of the deepest recursive 
        # call is equal to the height of the tree.
        # O(N) ~ for worst case size of prefix sum map



        prefixSum = defaultdict(int)

        prefixSum[0] = 1

        def dfs(root, curSum):

            if not root:
                return 0

            curSum += root.val

            count = prefixSum[curSum - targetSum]

            prefixSum[curSum] += 1

            count += dfs(root.left, curSum)
            count += dfs(root.right, curSum)

            prefixSum[curSum] -= 1

            return count

        return dfs(root, 0)
        