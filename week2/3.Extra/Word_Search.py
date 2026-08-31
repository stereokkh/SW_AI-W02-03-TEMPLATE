"""
check_list = [[0,0,0],[],[]]로 초기화
처음 시작자리 (i,j)
#base case
if i,j != 찾아야하는 글자:
    return

if i != 0 , (i-1, j)check == 0
    i-1,j
if i len(arr)-1, (i+1, j)check== 0
    i+1, j
if j!=0, (i, j-1)check == 0
    i, j-1
if j!=0, (i , j+1)check == 0
    i , j+1
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        word_board = [[0 for i in board[0]] for j in board]
        for x in range(len(board)):
            for y in range(len(board[0])):
                word_board[x][y] = 1
                if self.dfs(board, x, y, word, 0, word_board):
                    return True
                word_board[x][y] = 0

        
        return False

    """
    공간최적화
    word_board 삭제 board에서 값 temp 저장 값 = none 이후 temp로 복구
    
    """
    def dfs(self, board, x, y, word:str, word_cnt, word_board): #wordcnt
        if word[word_cnt] != board[x][y]:
            return

        if word_cnt == len(word)-1:
            return True
        #상하좌우 dfs
        if x-1 >= 0 and word_board[x-1][y] == 0:
            word_board[x-1][y] = 1
            if self.dfs(board, x - 1, y, word, word_cnt+1, word_board):
                return True
            word_board[x-1][y] = 0

        if x + 1 < len(board) and word_board[x+1][y] == 0:
            word_board[x+1][y] = 1
            if self.dfs(board, x+1, y, word, word_cnt+1, word_board):
                return True
            word_board[x+1][y] = 0

        if y-1  >= 0 and word_board[x][y-1] == 0:
            word_board[x][y-1] = 1
            if self.dfs(board, x, y-1 , word, word_cnt+1, word_board):
                return True
            word_board[x][y-1] = 0

        if y + 1 < len(board[0]) and word_board[x][y+1] == 0:
            word_board[x][y+1] = 1
            if self.dfs(board, x, y + 1, word, word_cnt+1, word_board):
                return True
            word_board[x][y+1] = 0
        


