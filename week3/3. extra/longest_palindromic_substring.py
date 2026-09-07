class Solution:
    def longestPalindrome(self, s: str) -> str:
        dic = [[0 for _ in s] for _ in s]
        max_l = 0
        max_l_index = (0,0)
        for jump in range(len(s)):
            for start in range(len(s)-jump):
                if jump <=1:
                    if s[start] == s[start+jump]:
                        dic[start][start+jump] = 1
                        if max_l < jump:
                            max_l = jump
                            max_l_index = (start ,start+ jump)
                
                else:
                    if s[start] == s[start+jump] and dic[start+1][start+jump-1] == 1:
                        dic[start][start+jump] = 1
                        if max_l < jump:
                            max_l = jump
                            max_l_index = (start ,start+ jump)

                    else : dic[start][start+jump] = 0
        return s[max_l_index[0] : max_l_index[1] + 1]
        

        

            
if __name__ == "__main__":
    s = "babad"
    a = Solution()
    len = a.longestPalindrome(s)
    print(len)
