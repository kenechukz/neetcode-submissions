class Solution:
    
    # Time: O(n log n + m)
    # Space: O(n)

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        l,r = 0, len(products)-1

        for i in range(len(searchWord)):
            
            # if i is out of range of product or current ch (searchWord[i]) is not
            # equal to current ch in product, we move pointer
            while l<=r and (i >= len(products[l]) or searchWord[i] != products[l][i]):
                l+= 1

            while l<=r and (i >= len(products[r]) or searchWord[i] != products[r][i]):
                r-=1

            res.append([])
            remain = (r-l) +1
            for j in range(min(3, remain)):

                res[-1].append(products[l+j])

        return res




        