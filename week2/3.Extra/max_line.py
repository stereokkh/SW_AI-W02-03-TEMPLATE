"""
직선으로 이을 수 있는 점의 최대 갯수
bruteforce?
y = b
y= ax + b
b = x
(x_1-x_2)y = (y_1 - y_2)x + b * (x_1-x_2)

"""
# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         max = 0 
#         for i in range(n):
#             for j in range(i+1,n,1):
#                 cnt = 0
#                 if is_vertical:
#                     for point in range(len(points)):
#                         if points[i][0] == point[0]:
#                             cnt += 1
#                 else:
#                     a, b = find_line(points[i][0], points[i][1], points[j][0], points[j][1])
#                     for point in range(len(points)):
#                         if a * point[0] + b - point[1] == 0:
#                             cnt+=1
#                 if max < cnt:
#                     max = cnt
#         return max
                

# def is_vertical(x_1, y_1, x_2, y_2):
#     if  x_1 - x_2 == 0:
#         return True
#     return False

# def find_line(x_1, y_1, x_2, y_2):
#     a = (y_1 - y_2)/(x_1 - x_2)
#     b = y_1 - a*x_1
#     return a, b

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        max_cnt = 0 
        if n == 1:
            return 1
        for i in range(n):
            inclines = {}
            for j in range(i+1,n,1):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == 0:
                    incline = 'vertical'
                else:
                    incline = dy/dx
                inclines[incline] = inclines.get(incline, 1) + 1
            if max(inclines.values(), default = 0) > max_cnt:
                max_cnt = max(inclines.values(), default = 0)
                  
        return max_cnt