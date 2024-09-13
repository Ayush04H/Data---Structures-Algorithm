from collections import deque

def orangesRotting(grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
    
        # Initialize the queue for BFS and count fresh oranges
        q = deque()
        fresh_oranges = 0
        
        # Step 1: Add all initial rotten oranges to the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  # Add rotten orange with its time (0 minutes)
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Directions for the 4-adjacent cells (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: Perform BFS to rot the adjacent fresh oranges
        minutes_elapsed = 0
        while q:
            r, c, minutes = q.popleft()
            minutes_elapsed = minutes  # Update the time for each level of BFS

            # Check all 4 adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    # Rot this fresh orange
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    q.append((nr, nc, minutes + 1))

        # Step 3: If there are still fresh oranges left, return -1
        if fresh_oranges > 0:
            return -1
        return minutes_elapsed




grid = [[2,1,1],[1,1,0],[0,1,1]]

print(orangesRotting(grid))