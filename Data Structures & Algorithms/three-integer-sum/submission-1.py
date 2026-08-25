class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        resp = set([])
        for i in range(len(sorted_nums) - 1):
            l, r = i + 1, len(sorted_nums) - 1
            target = -sorted_nums[i]
            while r > l:
                cal = sorted_nums[l] + sorted_nums[r]
                if cal == target:
                    resp.add((sorted_nums[i], sorted_nums[l], sorted_nums[r]))
                    l += 1
                    r -= 1
                elif cal < target:
                    l += 1
                else:
                    r -= 1

        return [list(t) for t in resp]
