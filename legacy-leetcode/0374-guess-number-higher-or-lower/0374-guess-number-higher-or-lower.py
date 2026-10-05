# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        # We need to guess a number between 1 and n using the guess() API.
        # The API returns -1 if the guess is too high, 1 if too low, and 0 if correct.
        # To minimize the number of guesses, we use binary search.
        # Start with the range [1, n].
        # On each iteration, compute the mid value.
        # Use guess(mid) to check if the number is too high, too low, or correct.
        # Narrow the search range accordingly.
        # When guess(mid) returns 0, we have found the correct number.
        # Time complexity: O(log n)
        # Space complexity: O(1)

        l = 1
        r = n
        mid = (l+r)//2
        while (True):
            if guess(mid) == 0:
                return mid
            # if mid > pick
            if guess(mid) == -1:
                r = mid-1
                mid = (l+r)//2
            #if mid < pick
            elif guess(mid) == 1:
                l = mid+1
                mid = (l+r)//2

        