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
        path = []
        def dfs(i):
            
            if i >= len(s):
                res.append(path[:])
                return
            for j in range(i,len(s)):
                curSub = s[i: j+1]
                if curSub == curSub[::-1]:
                    path.append(curSub)
                    dfs(j+1)
                    path.pop()

        dfs(0)
        return res
            

        






        