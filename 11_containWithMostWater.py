class Solution(object):
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        # height >> [1,8,6,2,5,4,8,3,7]
        # dist * min(l,r)
        # move the smaller_height pointer to achieve potential larger area
        l,r = 0,len(height) - 1
        area = 0
        while l < r:
            area = max(area,(r-l) * min(height[l],height[r]))
            if height[l] < height[r]:
                # smaller is l >> l need to move to righter
                l += 1
            else:
                r -= 1

        return area
    
heights = [1,8,6,2,5,4,8,3,7]
print(Solution.maxArea(heights))