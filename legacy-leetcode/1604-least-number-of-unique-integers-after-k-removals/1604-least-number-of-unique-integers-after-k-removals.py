from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        """
        R:

        return least number of unique elems left after k removals

        E:
        0 <= k <= arr.length

        A:

        arr = [4,3,1,1,3,3,2], k = 3

         4: 1, 2: 1, 1: 2, 3: 3
        total unique = len(dict)

        {(4, 1), (2, 1), (1, 2),(3, 3)}

        
        """


        count = Counter(arr)
        unique = len(count)

        arr = [[k, v] for k,v in count.items()]
        arr.sort(key=lambda x: x[1])

        i,j = 0,0
        
        while i < k and j < len(arr):
            arr[j][1] -= 1
            if arr[j][1] == 0:
                unique -=1
                j+=1
            i+=1

        return unique











