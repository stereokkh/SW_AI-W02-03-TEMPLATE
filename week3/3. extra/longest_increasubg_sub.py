class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        list_l = [1 for _ in nums]
        for i in range(1, len(nums)):
            max_num = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_num = max(list_l[j], max_num)
            list_l[i] += max_num
        max_l = 0
        for k in list_l:
            max_l = max(k, max_l)
        return max_l