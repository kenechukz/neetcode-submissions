class Solution:

    toInt ={"0":0, "1":1, "2":2, "3":3, "4":4, 
    "5":5, "6":6, "7":7, "8":8, "9":9}

    def convToInt(self, s, res):
        for ch in s:
            res *= 10
            res += self.toInt[ch]
        return res

    def multiply(self, num1: str, num2: str) -> str:

        intNum1 = intNum2 = 0
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 == "1":
            return num2
        elif num2 == "1":
            return num1

        return str(self.convToInt(num1, intNum1) * self.convToInt(num2, intNum2))
        