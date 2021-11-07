'''
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''


class Solution(object):
    '''
    GraphDFS: Time O(nm * 3^w) where n and m are the length of the row and colum in the board, and w is the length of the word. The reason why we have 3 directions are because we don't go back to the place where we come from.

    We want to iterate characters in the board and if the character is matching with the first character of the word, we want to traverse in dfs manner to find its neighbors to check if the word can be made.

    - Iterate the board characters and if the character is matched with the first character of the word, then create a visitedSet hashset and call a function to traverse dfs.
    - Base case is when our visitedSet length is equal to the length of the word, then set global variable found equal to true.
    - Check if the row and col are in the bounds, current character in the board is matched to the word character, and current row and col is not in visitedSet, then we want to append the current row and col into the visitedSet and traverse its neighbors(up, left, bottom, right), and at the end of the traverse, and make sure to remove the row and col element from the visitedSet.
    '''

    def exist(self, board, word):
        self.found = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.visitedSet = set()
                    self.traverseDFS(word, board, i, j, 0)
                    if self.found:
                        return True
        return False

    def traverseDFS(self, word, board, row, col, i):
        if len(self.visitedSet) == len(word):
            self.found = True

        if not self.found and row >= 0 and col >= 0 and row < len(board) and col < len(board[0]) and board[row][col] == word[i] and (row, col) not in self.visitedSet:

            self.visitedSet.add((row, col))

            self.traverseDFS(word, board, row-1, col, i+1)
            self.traverseDFS(word, board, row, col-1, i+1)
            self.traverseDFS(word, board, row+1, col, i+1)
            self.traverseDFS(word, board, row, col+1, i+1)

            self.visitedSet.remove((row, col))
