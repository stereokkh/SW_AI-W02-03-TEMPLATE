# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        list = []
        queue = deque()
        def bfs(point):
            if point == None:
                return []
            list.append([])
            list[0].append(point.val)
            if point.left != None:
                queue.append(point.left)
            if point.right != None:
                queue.append(point.right)      
            
            while queue:
                level = len(queue)
                list.append([])
                for _ in range(level):
                    current = queue.popleft()
                    list[-1].append(current.val)
                    if current.left != None:
                        queue.append(current.left)
                    if current.right != None:
                        queue.append(current.right)
            return

        bfs(root)
        return list