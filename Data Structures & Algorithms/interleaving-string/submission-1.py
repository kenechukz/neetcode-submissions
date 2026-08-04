class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # Initial Check: The lengths must sum up.
        if len(s1) + len(s2) != len(s3):
            return False

        # Memoization map: keys are (i, j) where i is the index in s1 and j is the index in s2.
        # k is implied by k = i + j.
        memo = {}

        # i: index in s1, j: index in s2
        def dfs(i, j):
            # Calculate the current index in s3
            k = i + j
            
            # 1. Correct Base Case: If we've successfully consumed all of s3 (k == len(s3)), 
            # and by extension all of s1 and s2, then we found a path.
            if k == len(s3):
                # Since we checked the total length initially, this is sufficient.
                return True
            
            # Check memo for the current state (i, j)
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Initialize the result for the current state
            res = False
            
            # 2. Path 1: Try to take the character from s1
            # Check bounds of s1 AND if s1[i] matches s3[k]
            if i < len(s1) and s1[i] == s3[k]:
                # Explore this path. If the recursive call returns True, the current state is True.
                res = dfs(i + 1, j)
            
            # 3. Path 2: Try to take the character from s2
            # Check bounds of s2 AND if s2[j] matches s3[k]
            # Use 'or' to check this path even if Path 1 was True (to explore both possibilities 
            # if s1[i] == s2[j] == s3[k]).
            if j < len(s2) and s2[j] == s3[k]:
                res = res or dfs(i, j + 1)
            
            # Store the final result for the current state before returning
            memo[(i, j)] = res
            return res

        # Start the recursive process from the beginning
        return dfs(0, 0)