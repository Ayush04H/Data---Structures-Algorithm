from collections import deque
def numEnclaves(grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = [[False] * cols for _ in range(rows)]
        
        # Add boundary land cells (1s) to the queue
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and grid[i][j] == 1:
                    q.append((i, j))
                    visited[i][j] = True
        
        # Directions for moving up, down, left, and right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS to mark all reachable cells from the boundary
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True

        # Count the number of enclaves
        enclave_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    enclave_count += 1

        return enclave_count



grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

print(numEnclaves(grid))
