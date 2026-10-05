class Solution:
    def partitionString(self, s: str) -> List[str]:

        """
        R:
        given string: s

        partition it into unique segments like so:

        if seg not seen before add to seen segments
        else extend it until it hasn't beenm seen

        E:
        1 <= s.length <= 10^5
        s contains only lowercase English letters.

        A:
        c = cur seg to check
        "abbccccd"
         c
         j
        """
        seen = set()
        res = []
        seg = ""
        for ch in s:
            seg += ch
            if not seg in seen:
                seen.add(seg)
                res.append(seg)
                seg = ""

        return res
            


        