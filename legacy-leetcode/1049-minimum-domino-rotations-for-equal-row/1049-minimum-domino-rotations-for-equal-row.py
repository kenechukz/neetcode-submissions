from collections import defaultdict
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        tops:       [2,1,2,4,2,2]
        bottoms:    [5,2,6,2,3,2]

        rotate top[1]
        rotate top[3]

        result - 2

        R:
        given top and bottom of dominoes

        return min no. rotations to till all tops or all bottoms are equal
        else -1

        E:
        assume top and bottom same length

        if already tops all equal or bottoms all equal: return 0
        if tops len == 1:
            return 0
        (Same as 1st edge)

        [5,3,5,5,3]
        [3,5,3,3,5]
        A:
        
        [2, 4]
        [5, 2]
                        [2, 5]

                    [2, 5]     [5,2]
                
            [4, 2]      [2, 4]

        recursively choose and unchoose 

        find the most popular number

        for valid solution -> should be at least tops many of that item between bottom and top

        [1,2,1,1,1,2,2,2]
        [2,1,2,2,2,2,2,2]

        
        Optimal:
        The only possible final numbers are:
        tops[0] or bottoms[0]
        Because any valid target must appear in at least one of every domino.
        So — just test both.

        e.g. for example 1 bottoms[0] isn't valid (once we get to 2nd iter i=1) on first if condition, 
        so we assign it infinity
        however for top[0], it is equal to tops[i] or bottoms[i] at each index
        so we return min of the rotations needed for the bottom and the rotations needed for the top
        """
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                if x != tops[i] and x != bottoms[i]:
                    return float('inf')  # impossible
                elif x != tops[i]:
                    rotations_top += 1
                elif x != bottoms[i]:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        ans = min(check(tops[0]), check(bottoms[0]))
        return ans if ans != float('inf') else -1


    

        





         

        

        

        





        