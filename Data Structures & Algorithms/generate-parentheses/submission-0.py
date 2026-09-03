class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(cur, l, r):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if l < n:
                recurse(cur + "(", l + 1, r)
            if r < l:
                recurse(cur + ")", l, r + 1)

        recurse("", 0, 0)
        return res