class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)-1
        left,right = 0 ,n
        max_area = 0

        while left<right:
            if height[left]<height[right]:
                area = height[left]*(right-left)
                max_area = max(max_area,area)
                left+=1
            else:
                area = height[right]*(right-left)
                max_area = max(max_area,area)
                right-=1


        return max_area                
