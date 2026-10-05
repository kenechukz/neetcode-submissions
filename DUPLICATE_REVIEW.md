# Duplicate solution review

`Data Structures & Algorithms/` is managed by NeetCode GitHub Sync. The
`legacy-leetcode/` contains the legacy-only import plus the approved legacy
and rewritten canonical solutions from this report. The legacy link points to
the original repository; the NeetCode path points to the synced submission(s).

## Decision guide

- **Exact** means the source code is byte-for-byte identical. No functional
  comparison is needed; use the recommendation unless you want to improve it.
- **Keep NeetCode** preserves the recommended synced submission as the
  canonical copy.
- **Keep legacy** means I will place the reviewed legacy implementation in the
  manual collection; it will not be overwritten by NeetCode Sync.
- **Rewrite** means neither existing version meets the problem's intended
  constraints. I will add a correct canonical implementation after you choose
  it.

## Overlaps

| Problem | Legacy | NeetCode | Status | Recommendation | Why |
| --- | --- | --- | --- | --- | --- |
| Two Sum | [Java](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0001-two-sum/0001-two-sum.java) | `two-integer-sum/submission-5.py` | Different | Keep NeetCode `submission-5.py` | Clear O(n) hash-map solution; legacy continues after finding the guaranteed pair. |
| Add Two Numbers | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0002-add-two-numbers/0002-add-two-numbers.py) | `add-two-numbers/submission-0.py` | Exact | Keep either | Identical correct O(n) implementation. |
| Longest Substring Without Repeating Characters | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0003-longest-substring-without-repeating-characters/0003-longest-substring-without-repeating-characters.py) | `longest-substring-without-duplicates/submission-0.py` | Different | Keep NeetCode | Both are O(n); NeetCode keeps the simpler sliding-window invariant. |
| Container With Most Water | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0011-container-with-most-water/0011-container-with-most-water.py) | `max-water-container/submission-0.py` | Different | Keep NeetCode | Both are O(n); NeetCode is more direct. |
| 3Sum | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0015-3sum/0015-3sum.py) | `three-integer-sum/submission-3.py` | Different | Keep NeetCode `submission-3.py` | Legacy can emit duplicate triplets; this version deduplicates correctly in O(n²). |
| Letter Combinations of a Phone Number | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0017-letter-combinations-of-a-phone-number/0017-letter-combinations-of-a-phone-number.py) | `combinations-of-a-phone-number/submission-0.py` | Different | Keep legacy | Direct backtracking; NeetCode explores unnecessary skipped-index branches. |
| Multiply Strings | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0043-multiply-strings/0043-multiply-strings.py) | `multiply-strings/submission-0.py` | Exact | Rewrite | Identical code uses arbitrary-size integer conversion, which violates the intended constraint. |
| Permutations | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0046-permutations/0046-permutations.py) | `permutations/submission-0.py` | Different | Keep legacy | Correct direct backtracking; NeetCode unnecessarily relies on distinct inputs via a set. |
| Merge Intervals | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0056-merge-intervals/0056-merge-intervals.py) | `merge-intervals/submission-0.py` | Different | Keep NeetCode | Both are O(n log n); NeetCode's interval invariant is more compact. |
| Insert Interval | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0057-insert-interval/0057-insert-interval.py) | `insert-new-interval/submission-0.py` | Exact | Keep either | Identical correct O(n) code. |
| Unique Paths | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0062-unique-paths/0062-unique-paths.py) | `count-paths/submission-0.py` | Different | Keep legacy | Same DP time; legacy uses O(n) rolling-row space rather than O(mn). |
| Plus One | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0066-plus-one/0066-plus-one.py) | `plus-one/submission-0.py` | Exact | Keep either | Identical correct carry propagation. |
| Binary Tree Level Order Traversal | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0102-binary-tree-level-order-traversal/0102-binary-tree-level-order-traversal.py) | `level-order-traversal-of-binary-tree/submission-0.py` | Exact | Rewrite | Identical `list.pop(0)` queue can degrade to O(n²); use `collections.deque`. |
| Maximum Depth of Binary Tree | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0104-maximum-depth-of-binary-tree/0104-maximum-depth-of-binary-tree.py) | `depth-of-binary-tree/submission-0.py` | Different | Keep legacy | Equivalent O(n) traversal with the fuller legacy explanation. |
| Best Time to Buy and Sell Stock | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0121-best-time-to-buy-and-sell-stock/0121-best-time-to-buy-and-sell-stock.py) | `buy-and-sell-crypto/submission-0.py` | Different | Keep NeetCode | Both are O(n); NeetCode avoids a redundant single-element special case. |
| Surrounded Regions | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0130-surrounded-regions/0130-surrounded-regions.py) | `surrounded-regions/submission-4.py` | Different | Keep NeetCode | Legacy can incorrectly flip part of a border-connected region. |
| Linked List Cycle | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0141-linked-list-cycle/0141-linked-list-cycle.py) | `linked-list-cycle-detection/submission-0.py` | Exact | Rewrite | Identical visited-set version is correct but uses O(n), not Floyd's O(1) extra space. |
| Number of Islands | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0200-number-of-islands/0200-number-of-islands.py) | `count-number-of-islands/submission-0.py` | Different | Keep NeetCode `submission-0.py` | Iterative BFS avoids recursion-depth failure on a large all-land grid. |
| Reverse Linked List | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0206-reverse-linked-list/0206-reverse-linked-list.py) | `reverse-a-linked-list/submission-0.py` | Exact | Keep either | Identical optimal O(n)-time/O(1)-space reversal. |
| House Robber II | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0213-house-robber-ii/0213-house-robber-ii.py) | `house-robber-ii/submission-1.py` | Different | Keep legacy | Both are O(n); legacy does not mutate working arrays. |
| Kth Largest Element in an Array | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0215-kth-largest-element-in-an-array/0215-kth-largest-element-in-an-array.py) | `kth-largest-element-in-an-array/submission-2.py`, `submission-3.py` | Different | Keep legacy | O(n log k) heap; one NeetCode submission lacks `math` import. |
| Top K Frequent Elements | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0347-top-k-frequent-elements/0347-top-k-frequent-elements.py) | `top-k-elements-in-list/submission-0.py` | Different | Keep NeetCode | Both use O(n) bucket sort; NeetCode is clearer. |
| Design Twitter | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0355-design-twitter/0355-design-twitter.py) | `design-twitter-feed/submission-5.py`, `submission-6.py` | Mixed | Rewrite | Exact heap versions omit usable `heapq`/`defaultdict` imports; the alternate is slower. |
| Non-overlapping Intervals | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/0435-non-overlapping-intervals/0435-non-overlapping-intervals.py) | `non-overlapping-intervals/submission-0.py` | Different | Keep legacy | Both use correct greedy logic; legacy has no unreachable trailing string. |
| K Closest Points to Origin | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/1014-k-closest-points-to-origin/1014-k-closest-points-to-origin.py) | `k-closest-points-to-origin/submission-0.py`, `submission-1.py` | Different | Keep legacy | NeetCode's versions call `math.sqrt` without importing `math`. |
| Longest Common Subsequence | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/1250-longest-common-subsequence/1250-longest-common-subsequence.py) | `longest-common-subsequence/submission-0.py` | Different | Keep NeetCode | Both are O(mn) DP; the recurrence is clearer. |
| Count Good Nodes in Binary Tree | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/1448-count-good-nodes-in-binary-tree/1448-count-good-nodes-in-binary-tree.py) | `count-good-nodes-in-binary-tree/submission-0.py` | Exact | Rewrite | Identical class-level counter leaks state across repeated calls. |
| Longest Increasing Subsequence | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/longest-incr-subsequence/main.py) | `longest-increasing-subsequence/submission-5.py`, `submission-6.py`, `submission-7.py` | Different | Keep legacy | Cleanest correct O(n²) DP, although an O(n log n) version would be better. |
| Maximum Subarray | [Python](https://github.com/kenechukz/LeetcodeDSA-Practice/blob/main/max_subarray.py) | `maximum-subarray/submission-0.py`, `submission-1.py` | Different | Keep legacy | Correct Kadane O(n) with the clearest invariant; NeetCode `submission-0.py` is O(n²). |

## Resolution

All recommendations were approved on 2026-10-05.

- **Keep legacy** selections and **Rewrite** fixes are in `legacy-leetcode/`.
- **Keep NeetCode** and **Keep either** selections remain only in the
  sync-managed `Data Structures & Algorithms/` directory.
- The original `LeetcodeDSA-Practice` repository remains unchanged as the
  historical source.
