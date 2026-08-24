class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        max_cons = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                current_num  = num
                while current_num in nums_set:
                    current_num += 1
                
                max_cons = max(max_cons, current_num - num)

        return max_cons

            
        