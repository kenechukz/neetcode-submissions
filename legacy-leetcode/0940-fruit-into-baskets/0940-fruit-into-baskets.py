class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
            tree 0 hold fruit 1
            tree 1 hold fruit 2
            tree 3 holds fruit 1

            look at counts?
            sliding window?

            fruits = [1,2,3,2,2,1,1,1,1]
                              L       R

        """

        count = total = l = 0
        unique = {}
        for r in range(len(fruits)):
            unique[fruits[r]] = unique.get(fruits[r], 0) + 1
            count +=1
            while len(unique) > 2:
                unique[fruits[l]] -= 1
                if unique[fruits[l]] <= 0:
                    del unique[fruits[l]]
                count -= 1
                l = l + 1
            total = max(total, count)
        return total