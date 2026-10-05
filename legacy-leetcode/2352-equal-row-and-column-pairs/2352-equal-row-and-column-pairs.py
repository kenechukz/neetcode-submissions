class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        # Approach:
        # 1. Initialize an empty hashmap (dictionary) to count how many times each row appears in the grid.
        # - Convert each row to a tuple (so it can be used as a dictionary key).
        # - Store the frequency of each unique row.
        # 2. For each column in the grid:
        # - Construct the column as a tuple by collecting the i-th element from each row.
        # - Check if this column tuple exists in the row hashmap.
        # - If it does, add the number of times this row appears (row_map[col]) to the result.
        # 3. Return the total count of row-column pairs that are equal.


        n = len(grid)
        row_map = {}
        for row in grid:
            key = tuple(row)
            row_map[key] = row_map.get(key, 0) + 1

        res = 0
        for i in range(n):
            col = tuple(grid[j][i] for j in range(n))
            if col in row_map:
                res += row_map[col]

        return res
