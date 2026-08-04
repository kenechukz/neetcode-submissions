class Solution:
    """
    R:
    given nums

    return len of longest incr. subsequence

    can delete some or no elements, but can't change relative order

    E:

    what if there are two subsequences of equal len -> take newer found one

    if new elem equal to prev, don't add to sequence
    Constraints:

    1 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000

    A:
        start seq: 9

        calls to 1

        1 < 9

        set max len

        start seq: 1


        calls to 4

        inc cur seq len

        seq: 1, 4

        calls 2

                        9

                    1

                2        4

            3      3           7
            
                7 



        maxLen = ?
        (i, len)

        [0,3,1,3,2,3]
        [4,3,3,2,2,1]
        if cur < next:
            # we add it to subsequence
            best[cur_idx] = 1+ best[next_idx]
        else:
            best[cur_idx] = best[next_idx]
        
        [9,1,4,2,3,3,7]
        [1,4,2,3,2,2,1]

        nums=
        [0,1,0,3,2,3]
        [,,,,2,1]

                   3
               0       2
                     1    0
                    0


    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        best = [1] * n

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    best[i] = max(best[i], 1 + best[j])

        return max(best)

        
        

        