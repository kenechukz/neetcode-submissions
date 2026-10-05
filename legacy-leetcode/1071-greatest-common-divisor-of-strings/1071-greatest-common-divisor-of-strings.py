class Solution:
    # Brute Force Solution
    """
        def gcdOfStrings(self, str1: str, str2: str) -> str:
            len1,len2 = len(str1),len(str2)
            
            
            def isDivisor(i):
                if len1 % i == 0 and len2 % i == 0:
                    f1,f2 = len1 // i, len2 // i
                    return str1[:i] * f1 == str1 and str1[:i] * f2 == str2


                else:
                    return False


            for i in range(min(len1,len2),0,-1):

                if isDivisor(i):
                    return str1[:i]


            return ""

        Time: O(min(m, n) × (m + n)), which is O(n²) when both strings are length `n`.
        Space: O(m + n), the splicing and concatenation of creates temporary strings

        We try up to min(m, n) possible prefix lengths. For each candidate, constructing and comparing its 
        repeated form against both `str1` and `str2` touches `m + n` characters total (len(str1) and len(str2)).

    """
    # Optimal Solution

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If we can't interchange strings, then they don't share the same base
        # this takes O(m + n) time since we have to look at all character of str 1 and str 2
        if str1 + str2 != str2 + str1:
            return ""

        # Underneath, this does euclid's algorithm 
        # this takes O(log(min(m, n)))
        divisor_length = gcd(len(str1), len(str2))
        return str1[:divisor_length]

    # Time: O(m+n)
    # Space: O(1)

    # Euclid's algorithm version
    """
    a = b
    b = a%b
    after each step

    a     b
    48 % 18 = 12  → (18, 12)
    18 % 12 = 6   → (12, 6)
    12 % 6 = 0    → (6, 0)
    """
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a, b = len(str1), len(str2)
        while b:
                a, b = b, a % b
        # Value of a at the end is the gcd

        return str1[:a]
        