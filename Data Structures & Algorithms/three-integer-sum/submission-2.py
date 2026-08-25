class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        resp = []
        for i in range(len(nums) - 2):

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            while r > l:
                cal = nums[l] + nums[r]
                if cal == target:
                    resp.append([nums[i], nums[l], nums[r]])
                    

                    cur_l, cur_r = nums[l], nums[r]
                    while r > l and cur_l == nums[l]:
                        l += 1
                    while r > l and cur_r == nums[r]:
                        r -= 1
                elif cal < target:
                    l += 1
                else:
                    r -= 1

        return resp
