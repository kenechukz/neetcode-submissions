# Canonical solutions

This index is the quick reference for problems that exist in both source
collections. Follow the **canonical path** when revising a problem.

`Data Structures & Algorithms/` is managed by NeetCode GitHub Sync.
`legacy-leetcode/` is manual content and will not be overwritten by sync.
For the detailed comparison and rejected alternatives, see
[DUPLICATE_REVIEW.md](DUPLICATE_REVIEW.md).

| Problem | Canonical path | Origin | Complexity | Why this is the canonical solution |
| --- | --- | --- | --- | --- |
| Two Sum | `Data Structures & Algorithms/two-integer-sum/submission-5.py` | NeetCode | O(n) | Clear hash-map lookup. |
| Add Two Numbers | `Data Structures & Algorithms/add-two-numbers/submission-0.py` | NeetCode (identical) | O(n) | Both versions were byte-identical. |
| Longest Substring Without Repeating Characters | `Data Structures & Algorithms/longest-substring-without-duplicates/submission-0.py` | NeetCode | O(n) | Simpler sliding-window invariant. |
| Container With Most Water | `Data Structures & Algorithms/max-water-container/submission-0.py` | NeetCode | O(n) | Direct two-pointer solution. |
| 3Sum | `Data Structures & Algorithms/three-integer-sum/submission-3.py` | NeetCode | O(n²) | Correctly deduplicates triplets. |
| Letter Combinations of a Phone Number | `legacy-leetcode/0017-letter-combinations-of-a-phone-number/0017-letter-combinations-of-a-phone-number.py` | Legacy | O(4ⁿ × n) | Direct backtracking without skipped-index branches. |
| Multiply Strings | `legacy-leetcode/0043-multiply-strings/0043-multiply-strings.py` | Rewritten | O(mn) | Grade-school multiplication without integer conversion. |
| Permutations | `legacy-leetcode/0046-permutations/0046-permutations.py` | Legacy | O(n × n!) | Direct backtracking without relying on a set. |
| Merge Intervals | `Data Structures & Algorithms/merge-intervals/submission-0.py` | NeetCode | O(n log n) | Compact, correct merge invariant. |
| Insert Interval | `Data Structures & Algorithms/insert-new-interval/submission-0.py` | NeetCode (identical) | O(n) | Both versions were byte-identical. |
| Unique Paths | `legacy-leetcode/0062-unique-paths/0062-unique-paths.py` | Legacy | O(mn) time, O(n) space | Uses a rolling DP row. |
| Plus One | `Data Structures & Algorithms/plus-one/submission-0.py` | NeetCode (identical) | O(n) | Both versions were byte-identical. |
| Binary Tree Level Order Traversal | `legacy-leetcode/0102-binary-tree-level-order-traversal/0102-binary-tree-level-order-traversal.py` | Rewritten | O(n) | Uses `deque` rather than O(n) front pops. |
| Maximum Depth of Binary Tree | `legacy-leetcode/0104-maximum-depth-of-binary-tree/0104-maximum-depth-of-binary-tree.py` | Legacy | O(n) | Equivalent traversal with the fuller explanation. |
| Best Time to Buy and Sell Stock | `Data Structures & Algorithms/buy-and-sell-crypto/submission-0.py` | NeetCode | O(n) | Avoids redundant special cases. |
| Surrounded Regions | `Data Structures & Algorithms/surrounded-regions/submission-4.py` | NeetCode | O(mn) | Avoids a border-region correctness bug in legacy. |
| Linked List Cycle | `legacy-leetcode/0141-linked-list-cycle/0141-linked-list-cycle.py` | Rewritten | O(n) time, O(1) space | Floyd's tortoise-and-hare algorithm. |
| Number of Islands | `Data Structures & Algorithms/count-number-of-islands/submission-0.py` | NeetCode | O(mn) | Iterative BFS avoids recursion-depth failures. |
| Reverse Linked List | `Data Structures & Algorithms/reverse-a-linked-list/submission-0.py` | NeetCode (identical) | O(n) time, O(1) space | Both versions were byte-identical. |
| House Robber II | `legacy-leetcode/0213-house-robber-ii/0213-house-robber-ii.py` | Legacy | O(n) | Avoids mutating its working arrays. |
| Kth Largest Element in an Array | `legacy-leetcode/0215-kth-largest-element-in-an-array/0215-kth-largest-element-in-an-array.py` | Legacy | O(n log k) | Correct min-heap implementation. |
| Top K Frequent Elements | `Data Structures & Algorithms/top-k-elements-in-list/submission-0.py` | NeetCode | O(n) | Clear bucket-sort implementation. |
| Design Twitter | `legacy-leetcode/0355-design-twitter/0355-design-twitter.py` | Rewritten | O((F + 10) log F) per feed | Correct heap merge with module-level imports. |
| Non-overlapping Intervals | `legacy-leetcode/0435-non-overlapping-intervals/0435-non-overlapping-intervals.py` | Legacy | O(n log n) | Correct greedy implementation without dead code. |
| K Closest Points to Origin | `legacy-leetcode/1014-k-closest-points-to-origin/1014-k-closest-points-to-origin.py` | Legacy | O(n log n) | Working distance sort; NeetCode versions lack an import. |
| Longest Common Subsequence | `Data Structures & Algorithms/longest-common-subsequence/submission-0.py` | NeetCode | O(mn) | Clearest DP recurrence. |
| Count Good Nodes in Binary Tree | `legacy-leetcode/1448-count-good-nodes-in-binary-tree/1448-count-good-nodes-in-binary-tree.py` | Rewritten | O(n) | Per-call state prevents counter leakage. |
| Longest Increasing Subsequence | `legacy-leetcode/longest-incr-subsequence/main.py` | Legacy | O(n²) | Cleanest correct existing DP solution. |
| Maximum Subarray | `legacy-leetcode/max_subarray.py` | Legacy | O(n) | Correct Kadane implementation. |
