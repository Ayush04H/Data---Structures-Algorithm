from collections import deque
def solve(board: list[list[str]]) -> None:
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        q = deque()

        # Step 1: Mark 'O's on the borders and their connected 'O's
        def mark_border_o(x, y):
            if board[x][y] == 'O':
                q.append((x, y))
                board[x][y] = 'B'  # Mark the 'O' connected to the border

        # Check the borders for 'O's and mark them
        for i in range(rows):
            mark_border_o(i, 0)  # Left border
            mark_border_o(i, cols - 1)  # Right border
        for j in range(cols):
            mark_border_o(0, j)  # Top border
            mark_border_o(rows - 1, j)  # Bottom border

        # BFS to mark all 'O's connected to the border
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'O':
                    q.append((nx, ny))
                    board[nx][ny] = 'B'  # Mark as 'B' (border-connected 'O')

        # Step 2: Flip all remaining 'O's to 'X', and 'B's back to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # Flip surrounded 'O' to 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'  # Flip 'B' back to 'O' (border-connected)

        return board


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

print(solve(board))