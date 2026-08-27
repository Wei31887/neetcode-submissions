class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        amt = 0
        stack = []
        for i in range(len(height)):
            curH = height[i]
            while stack and curH >= height[stack[-1]]:

                buttonIdx = stack.pop()
                if not stack:
                    continue
                
                leftIdx = stack[-1]
                
                area = (i - leftIdx - 1) * (min(height[leftIdx], curH) - height[buttonIdx])
                amt += area

            stack.append(i)
        
        return amt
