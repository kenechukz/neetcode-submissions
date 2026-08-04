class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(t) != len(s):
            return False
        for ch in s:
            
            if not ch in s_dict:
                s_dict[ch] = 1

            else:
                s_dict[ch]+= 1

        for ch in t:
        
            if not ch in t_dict:
                t_dict[ch] = 1

            else:
                t_dict[ch]+= 1

        return s_dict == t_dict   
        
        