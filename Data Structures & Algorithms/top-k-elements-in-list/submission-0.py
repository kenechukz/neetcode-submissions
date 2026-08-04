from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        R:
        return k most freq
        always unique answer

        E:
        if k =2 and [1, 2, 1, 3, 2, 3]
        1: 2
        2: 2
        3: 2
        
        


    
        A:
        have a count hash map - O(n) space
        make it an array of tuples - O(n) space
            for k,v in map.items() - O(len(map))
                arr.append(k, v)
        heapify array, sorting by last index O(n)
        pop k elements from heap: k log n
        time: O(k log n)
        space: O(n)

        Optimal:
        have a count hash map - O(n) space
        create a bucket array size n+1, where index corresponds to freq
        + populate it using freq of cur num as index and adding cur num to bucket at taht index
        build a res array, by adding from end of bucket array (where high freq is), add all elements from that bucket while
        len(res) < k

        Time:O(n)
        Space:O(n)
        
        
        """

        count = Counter(nums)
        n = len(nums)
        bucket_arr = [[] for _ in range(n+2)]

        for num,freq in count.items():
            bucket_arr[freq].append(num)
        res = []
        for i in range(n+1, -1,-1):
            bucket = bucket_arr[i]
            for x in bucket:
                if len(res) ==k:
                    return res
                res.append(x)
        return res
 


        