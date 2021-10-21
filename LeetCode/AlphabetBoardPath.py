'''
1138. Alphabet Board Path

On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
'''
'''
1. Hashmap and an array
- Create a hashmap where alphabet as a key and (r,c) position as a value with loop
- iterate char in given target string
    - Call movePositionAndUpdateString function where take currentIndex and targetIndex as arguments
        - Calculate movements(ups, lefts, rights, downs) and add the number of "U","L","R","D" char * movements
        - append "!" at the end
        - return that string
    - Add the returned string to the result
'''
target = "leet"
# Time O(n) Space O(n)


def alphabetBoardPath(target):
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
    boardMap = {}
    for row in range(len(board)):  # Time O(1) constant
        for col in range(len(board[row])):
            boardMap[board[row][col]] = (row, col)

    currentIndex = (0, 0)
    res = ""
    for char in target:  # Time O(n)
        targetIndex = boardMap[char]
        # Time O(1)  Space O(n)
        res += movePositionAndUpdateString(currentIndex, targetIndex)
        currentIndex = targetIndex
    return res


def movePositionAndUpdateString(currentIndex, targetIndex):
    currentRow, currentCol = currentIndex
    targetRow, targetCol = targetIndex
    str = ""
    ups = max(0, currentRow - targetRow)
    lefts = max(0, currentCol - targetCol)
    rights = max(0, targetCol - currentCol)
    downs = max(0, targetRow - currentRow)
    str += "U" * ups + "L" * lefts + "D" * downs + "R" * rights + "!"

    return str


print(alphabetBoardPath(target))
