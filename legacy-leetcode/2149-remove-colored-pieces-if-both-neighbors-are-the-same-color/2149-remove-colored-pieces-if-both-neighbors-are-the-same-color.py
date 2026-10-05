class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        """
        R:
        A - Alice
        B - Bob

        can remove from str[1:-1]
        and if neighbouring pieces equal to player

        return True alice wins, else False bob wins

        E:
        if len < 3:
            return False

        A:

        O(n^2)
        """
        aliceMoves = 0
        bobMoves = 0

        if len(colors) < 3:
            return False
        for i in range(1,len(colors)-1):

            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == "A":
                    aliceMoves +=1

                else:
                    bobMoves +=1

        return aliceMoves > bobMoves
        



        