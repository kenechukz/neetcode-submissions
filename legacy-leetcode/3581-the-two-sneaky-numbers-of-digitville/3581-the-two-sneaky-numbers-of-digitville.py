class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        seen = set()

        res = []
        for num in nums:
            if len(res) == 2:
                return res
            if num in seen:
                res.append(num)
            else:
                seen.add(num)
        return res