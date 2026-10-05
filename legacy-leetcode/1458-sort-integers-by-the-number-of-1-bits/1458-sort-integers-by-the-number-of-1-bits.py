class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        """
        R:

        sort by asc. num of 1's in binary rep.

        return array after sorting


        E:
        if xBin.count == yBin.count:
            sort by x and y

        if len arr == 1:
            return arr


        A:

        [0,1,2,3,4,5,6,7,8]

        []
        
        """
        
        arr.sort(key=lambda x: (bin(x)[2:].count("1"), x))
        return arr