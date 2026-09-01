"""
문제 이해
n*n 행렬 0, 1만 존재
루트노드는 gird 주소

노드 데이터 구조
val : 노드가 1이면 true, 0이면 false
isleaf : 잎노드면 ture 노드 4개 있으면 false

노드 좌상, 우상, 좌하, 우하

"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.split_quad((0,0), (n-1,n-1), grid)
        

        
    def split_quad(self, start, end, grid): #start = (start, start) / end = (end, end)
        if start == end:
            
            return Node(grid[start[0]][start[1]], 1, None, None,None,None)
        
        mid = ((start[0] + end[0])//2 , (start[1] + end[1] )//2)
        #출력 = 위에서부터 왼쪽에서 오른쪽
        #좌상 우상 좌하 우상
        ul = self.split_quad(start, mid, grid)
        
        ur = self.split_quad((start[0], mid[1] + 1), (mid[0], end[1]), grid)
        
        dl = self.split_quad((mid[0]+1,start[1]), (end[0], mid[1]), grid)
    
        dr = self.split_quad((mid[0]+1, mid[1]+1), end, grid)
        
        if ul.val == ur.val == dl.val == dr.val and ul.isLeaf == ur.isLeaf == dl.isLeaf == dr.isLeaf == 1:
            return Node(grid[mid[0]][mid[1]],1, None, None,None,None)

        return Node(grid[end[0]][end[1]], 0, ul, ur, dl, dr)
        


        
    



    



        