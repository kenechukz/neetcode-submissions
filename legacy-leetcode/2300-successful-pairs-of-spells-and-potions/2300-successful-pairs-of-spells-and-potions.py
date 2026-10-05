class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # For each spell, we want to count how many potions can pair with it such that:
        # spell * potion >= success
        # Naively checking each pair would be O(n * m), which is too slow for large inputs.
        # Instead, we:
        # 1. Sort the potions array in ascending order. This allows us to use binary search.
        # 2. For each spell, use binary search to find the **leftmost index** in potions such that:
        # spell * potions[i] >= success
        # This gives us the count of valid potions as:
        # len(potions) - index
        # 3. We store this count directly in the original spells array for output.
        # Time Complexity:
        # Sorting potions: O(m log m)
        # Binary search for each spell: O(n log m)
        # Total: O(m log m + n log m)

        potions.sort() # mlogm
        for i in range(len(spells)):
            partition = len(potions) 
            l,r = 0,len(potions)-1            
            while (l <= r):
                m = (l+r)//2
                if spells[i] * potions[m] >= success:
                    partition = min(partition, m)
                    r = m-1
                else:
                    l = m+1
            spells[i] = len(potions) - partition 
        return spells



        