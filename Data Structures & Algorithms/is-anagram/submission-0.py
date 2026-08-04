class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        return s == t
        """
        s_dict = {}
        t_dict = {}

        for ch in s:
            
            if not s in s_dict:
                s_dict[ch] = 1

            else:
                s_dict[ch]+= 1

        for ch in t:
        
            if not t in t_dict:
                s_dict[ch] = 1

            else:
                t_dict[ch]+= 1

        return s_dict == t_dict   
        """ 
        
        