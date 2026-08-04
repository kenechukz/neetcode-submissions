class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        """
        R:
        return all subsets of nums

        constr: 1<= nums.length <= 10

        E:
        if [] - > []

        A:[1 2 3]

                 1
        [] /           \ [1]
          2                2          
     [] /    \ [2]         [1]/   \ [1, 2]
       3        3           3      3
      / \      /  \         / \        / \
    []   [3]   [2] [2,3]   [1] [1, 3] [1,2]  [1, 2, 3]


         subsets: 2^n
         time complexity: (2^n)
        """

        res = []
        n = len(nums)

        def backtrack(i, temp):

            if i >= n:
                res.append(temp)
                return
            backtrack(i+1, temp)
            backtrack(i+1, temp + [nums[i]])




        backtrack(0, [])

        return res



    
        