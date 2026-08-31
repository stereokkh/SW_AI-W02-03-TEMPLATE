"""
h_index 는 한 사람이 쓴 논문들에 대해서 각 논문들은 인용된 횟수를 고려하여 최소 h회 이상 인용된 논문이 h편 이상일 때의 값을 h_index라 한다.
논문각 인용 횟수 = [3, 4, 2, 0 , 0, 1]
h_index = 2
"""

class Solution:
    #O(n^2)
    def hIndex(self, citations: List[int]) -> int:
        h_list = [0] * (len(citations) + 1)
        for i in citations:
            if i < len(citations):
                for j in range(i + 1):
                        h_list[j] += 1
            else:
                 for j in range(len(h_list)):
                      h_list[j] += 1
        cnt = 0
        max = 0
        for i in h_list:
            if i >= cnt:
                 max = cnt
            cnt += 1

        return max
    #O(nlogn)
    def hIndex_2(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        if not citations:
             return 0
        cnt = 0
        for i in citations:
             if cnt > i:
                  return cnt
             cnt += 1
        return cnt
    #O(n)
    def hIndex_3(self, citations: list[int]) -> int:
        n = len(citations)
        arr = [0]*(n+1)
        for citation in citations:
            if citation >= n:
                 arr[n] += 1
            else:
                 arr[citation] += 1
        cnt = 0
        for i in range(len(arr)-1, -1, -1):
             cnt += arr[i]

             if cnt >= i:
                  return i