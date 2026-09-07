# Definition for a binary tre node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        오른쪽 고를래 왼쪽 고를래 둘다 고르고 컷
        """
        max_pick = float('-inf')
        def dfs(point):
            left = 0
            right = 0
            nonlocal max_pick
            if point.left == None and point.right==None:
                max_pick = max(point.val, max_pick)
                return point.val

            if point.left != None:
                left = max(dfs(point.left), 0)
            if point.right != None:
                right = max(dfs(point.right), 0)

            max_pick = max(left + right + point.val, max_pick)

            return point.val+max(left, right, 0)
        dfs(root)
        return max_pick
