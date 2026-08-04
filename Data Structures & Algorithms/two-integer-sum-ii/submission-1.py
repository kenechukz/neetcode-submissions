class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """
        R:
        given: sorted array
        need to be O(1)

        return 1-indexed of two indices that add to target

        cons: 
        2<= nums.length <= 1000
        -1000 <= numbers[i] <= 1000
        -1000 <= target <= 1000
        E:
        if len  nums == 2:
            return target == nums[0] + nums[1]

        -190 -(-100) = -90
        -100 -90
        A:


        [1, 2, 3, 5] target =5
         l        r
        if curSum > target
            r-=1

        if curSum < target
            l+=1



        [2, 3 ,4] t= 7


        [1, 2, 6, 9, 12] target = 15
         l             
            r
         l     r   r   r
            l  l
                   r  

        [1, 2, 3, 5] target =5
         l  r

         r+=1 while < n and nums[l] + nums[r] < target
        
        if out of bounds and still lt target:
            inc l till while we lt target



         target - nums[l] = nums[r]

         5 - 1 = 4 != 2
         we increment r for cur l till nums[r] > target
         once nums[r] > target:
            we reset r to 

        """
        n = len(numbers)
        l,r =0,n-1

        while l < r:
            curSum =  numbers[l] + numbers[r]

            if curSum > target:
                r-=1
            elif curSum < target:
                l+= 1
            else:
                return [l+1, r+1]

        return []







        