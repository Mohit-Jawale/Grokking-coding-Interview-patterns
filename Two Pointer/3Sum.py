class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twosum(target_value,i):
            left = i+1
            right = len(nums)-1
            res1 = []
            while left<right:
                if (nums[left]+nums[right])<target_value:
                    left+=1
                elif(nums[left]+nums[right])>target_value:
                    right-=1 
                else:
                    res1.append([nums[left],nums[right],nums[i]])
                    left+=1
                    right-=1

            return res1

        nums.sort() #O(nlogn)
        res = []
        for i in range(len(nums)):#O(n)
            ans = twosum(-nums[i],i)
            if ans:
                for arr in ans:
                    arr.sort()
                    if arr not in res:
                        res.append(arr)
          
               
        return res
        
