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
         l  r
               r  r
            l  r  


         target - nums[l] = nums[r]

         5 - 1 = 4 != 2
         we increment r for cur l till nums[r] > target

        """
        n = len(numbers)
        if len(numbers) == 2:
            return [1, 2]

        for i in range(n):
            for j in range(i+1, n):
                if target - numbers[i] == numbers[j]:
                    return [i+1, j+1]


        