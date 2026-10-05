class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        """
        We start from the finish point and work backwards to determine the "recursive rule"
        We now all the rows and columns aligned with the finish point (as in row m-1 and col n-1)
        will have 1 way of reaching finish.
        Because of this we start from row m-2 and calculate it's no. of ways of reaching finish by
        summing the cell directly below cur cell with column 1 ahead of cur cell.

        Time: O(n * m)
        Space: O(n)
        """

        prevRow = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + prevRow[j]

            prevRow = newRow

        return prevRow[0]
