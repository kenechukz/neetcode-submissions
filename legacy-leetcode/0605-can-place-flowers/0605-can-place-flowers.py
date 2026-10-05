class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        if len(flowerbed) == 1 :
            if (n==1 and flowerbed[0] == 0):
                return True 
        
        for i in range(len(flowerbed)):

            if count == n:
                return True

            # Check adjacent only in front
            if  i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    count+=1
                    flowerbed[i] = 1

            
            #Check adjacent only behind
            elif i == len(flowerbed)-1:
                if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                    count+=1
                    flowerbed[i-1] = 1

            
            elif flowerbed[i] == 0 and (flowerbed[i+1] == 0 and flowerbed[i-1] == 0):
                count+=1
                flowerbed[i] = 1


        return count == n

        