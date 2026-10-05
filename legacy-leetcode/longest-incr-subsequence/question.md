# Longest Increasing Subsequence (LIS) — NeetCode

**Difficulty:** Medium

## Problem

Given an integer array `nums`, return the length of the **longest strictly increasing subsequence**.

A **subsequence** is formed by deleting some (or none) elements without changing the order of the remaining elements.

### Examples

#### Example 1

- Input: `nums = [9,1,4,2,3,3,7]`
- Output: `4`
- Explanation: One LIS is `[1,2,3,7]`.

#### Example 2

- Input: `nums = [0,3,1,3,2,3]`
- Output: `4`

### Constraints

- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`

### Target Complexity

Aim for **O(n²)** time or better.

### Notes / Approach Ideas

- DP (classic): `dp[i] = length of LIS ending at i`
  - Transition: `dp[i] = 1 + max(dp[j])` for all `j < i` where `nums[j] < nums[i]`
  - Answer: `max(dp)`
- (Optional faster) Patience sorting / binary search:
  - Maintain `tails[k] = smallest possible tail value of an increasing subsequence of length k+1`
  - Update with binary search → **O(n log n)**

---
Source: NeetCode — Longest Increasing Subsequence
