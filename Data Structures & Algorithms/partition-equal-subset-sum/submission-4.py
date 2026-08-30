class Solution:

    """

    dp[s] = we can form sum s from using some of the numbers so far

    nums = [1, 5, 11, 5], sum = 22, target = 11.

    . = F 
    sum:  0  1  2  3  4  5  6  7  8  9 10 11
    init  T  .  .  .  .  .  .  .  .  .  .  .

    Only sum 0 is reachable (empty subset).

    n = 1 — walk s from 11 down to 1. Every dp[s-1] is False except at the end:

    s=1:  dp[1] |= dp[0]   .|T → T   ← FLIP

        0  1  2  3  4  5  6  7  8  9 10 11
        T  T  .  .  .  .  .  .  .  .  .  .

    Reachable subsets: {}, {1}

    n = 5; s from 11 down to 5:

    s=6:  dp[6] |= dp[1]   .|T → T   ← FLIP   (1 + 5)
    s=5:  dp[5] |= dp[0]   .|T → T   ← FLIP   (0 + 5)

        0  1  2  3  4  5  6  7  8  9 10 11
        T  T  .  .  .  T  T  .  .  .  .  .

    Reachable: {}, {1}, {5}, {1,5} = 6


    n = 11; s from 11 down to 5:

    s=11:  dp[11] |= dp[0]   .|T → T   ← FLIP   (0 + 11)

        0  1  2  3  4  5  6  7  8  9 10 11
        T  T  .  .  .  T  T  .  .  .  .  T

    Reachable: {}, {1}, {5}, {1,5} = 6, {11} 

    n = 5 (the second one) — s from 11 down to 5:

    s=10: dp[10] |= dp[5]  .|T → T  ← FLIP   (5 + 5)

Subset sum recall card

1. Reframe: Two equal halves = one subset hitting `total/2`. The rest is forced. Odd total, return False.

2. Collapse: 2ⁿ subsets, but only `target+1` sums. Same sum = interchangeable (multiple sets can have the same sum). Key state on the sum, not the subset.

3. Track reachable sums: `dp[s]` = "can I hit `s`". Start `{0}`. Each `n` unions the set with itself shifted by `n`.

4. Descend: `dp[s]` reads `dp[s-n]`. Going down keeps that cell pre-`n`, so each number is used once. Ascending = unbounded knapsack.

Trigger: "pick some items to hit exactly X" → boolean array over sums, loop descending.

    
    """

    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)

        dp[0] = True
        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]