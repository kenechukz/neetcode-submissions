class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
        R:
        given: sorted nums1 - (m+n), nums2 - n
        return sorted in nums1 (extra n in nums1 is to accomodate nums2)
        constraints:
        0<= m,n <= 200
        1<= m+n <= 200

        E:
        if n == 0:
            return nums1
        if m ==0:
            return num2
        A:
        nums1 = [1, 4, 6, 0, 0, 0], nums2 = [2, 3, 5]

        brute force:
        add nums2 in nums1 from index m of nums1 O(n)
        sort (n log n)
        overall: n log n

        efficient method:
        nums1 = [1, 4, 5, 0, 0, 0], nums2 = [2, 3, 6]
                       n1            
                                e                        
                                                    n2   

        nums1 = [1, 2, 3, 4, 5, 6], nums2 = [2, 3, 6]   
 
                [1, 2, 3, 4, 5, 6]
                       n1    
                                e


                if nums1[n1] <= nums2[n2]:
                    n1+= 1
                else:
                    nums[n1] = nums[n2]
                    n2+=1 

        T:
        nums1 = [1,2,3,0,10,11,12], nums2 = [1, 2, 3, 5]
                

        """
        e = (m+n) -1

        while m > 0 and n > 0:

            if nums1[m-1] <= nums2[n-1]:
                nums1[e] = nums2[n-1]
                n-=1
            else:
                nums1[e] = nums1[m-1]
                m-=1

            e-=1
        
        while n > 0:
            nums1[e] = nums2[n-1]
            e-=1
            n-=1

        return nums1


        return nums1 
        