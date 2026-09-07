class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) +1
        return dp[len(dp)-1][len(dp[0])-1]




    

        # if word1[word1_i] == word2[word2_i]:
        #     word1_i += 1
        #     word2_i += 1



        # if word1[word1_i] != word2[word2_i]:
        #     #삭제
        #     word1_i += 1
        #     dp[word1_i - 1][word2_i]
        #     #삽입
        #     word2_i += 1
        #     dp[word1_i][word2_i-1]
        #     #변경
        #     word1_i += 1
        #     word2_i += 1
        #     dp[word1_i - 1][word2_i -1]

            

                    
                



           
