class Solution:
    def goodNodes(self, root) -> int:
        def count(node, maximum):
            if node is None:
                return 0

            is_good = node.val >= maximum
            next_maximum = max(maximum, node.val)
            return (
                is_good
                + count(node.left, next_maximum)
                + count(node.right, next_maximum)
            )

        return count(root, float("-inf"))
