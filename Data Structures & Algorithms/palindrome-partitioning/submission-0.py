class Solution:
    def partition(self, s: str) -> List[List[str]]:

        """
        R:
        given s: str

        return a list 

        E:
        if len == 1: return s[0]

        if curStr.ispalindrome and len :
            add to output
        if depth == len(s):
            return 
        A:
                    aab
     i = 0      a   aa     aab
       = 1    a  ab  b      
       = 2   b

        valid paths: [a, a, b] [aa, b]
       
                
        
        """

        res = []
        
        def dfs(i, path):
            
            if i >= len(s):
                res.append(path)

            for j in range(i,len(s)):
                curSub = s[i: j+1]
                if curSub == curSub[::-1]:
                    dfs(j+1, path + [curSub])

        dfs(0, [])
        return res
            

        






        