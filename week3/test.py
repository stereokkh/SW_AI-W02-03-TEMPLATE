class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = 0
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]

if __name__ == "__main__":

    num = [1,1,2,3,4,4,5,]
    num = set(num)
    for i in letter:
        print(i)

    
    