"""
문제 이해
사탕주기
각 사람에게 1개 이상 줘야한다
이웃보다 높은 숫자를 가지는 사람은 그 사람보다 사탕이 많아야 한다.
※숫자가 같으면 옆사람 상관 없다
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        c_list = []
        for i in range(len(ratings)):
            if i == 0:
                c_list.append(1)
                continue
            if ratings[i] > ratings[i-1]:
                c_list.append(c_list[i-1]+1)
            else:
                c_list.append(1)
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                c_list[i] = max(c_list[i+1] + 1, c_list[i])
        return sum(c_list)