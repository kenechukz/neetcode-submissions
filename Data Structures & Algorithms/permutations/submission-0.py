class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """
        R:
        given nums - int

        return all perms. (in any order)

        E:
        if length nums == 1 -> return single elem
        if cur == i?

        base cases:
            if curPerm == n -> add to res

        A:
                    [1 2 3]
                         []
                    1            2
                 [2 3]          [1 3]
                1 2      1 3      2 1     2 3
                [3]       [2]       [3]     [1]
                1 2 3     1 3 2     2 1 3    2 3 1

        pass a set to each rec. call and remove as needed


        """


        res = []

        def backtracking(curPerm, numSet):

                if not numSet:
                    res.append(curPerm)
                    return
                for num in numSet:
                    backtracking(curPerm + [num], numSet - {num})

                return





        backtracking([], set(nums))        
        return res