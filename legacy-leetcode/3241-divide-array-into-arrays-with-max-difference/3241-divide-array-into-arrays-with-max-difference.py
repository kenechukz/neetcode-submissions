class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        """
        R:
        given nums array of size n
        n is a multi. of 3

        divide nums into n/3 no. of arrays

        where diff between any two elems is in array <= k

        return 2D array containing the arrays

        E:

        if less than n/3 no. arrays produced ? -> return []

        1 <= n <= 10^5 - O(n log n or n^2) solution at worst probably

        A:
        [1,3,4,8,7,9,3,5,1]  k = 2

        sort
        [1,1,3,3,4,5,7,8,9]

        form groups 
        [[1,1,3],[3,4,5],[7,8,9]]

        if in any group group[2] - group[0] > k, we return []


        [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11] k = 14

        sort
        [2,2,2,]
        """
        n = len(nums)
        nums.sort()
        groups = []
        for i in range(0,n-2, 3):
            groups.append(nums[i: i+3])

        for group in groups:
            if group[2] - group[0] > k:
                return []
        return groups



        


        