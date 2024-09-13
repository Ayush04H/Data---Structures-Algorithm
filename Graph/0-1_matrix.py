from collections import deque
def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])

        dist = [[float('inf')] * cols for _ in range(rows)]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((1,j))

        direction = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            x,y = q.popleft()

            for dx,dy in direction:
                nx , ny = dx + x, dy + y
                if 0<=nx<rows and 0<=ny<cols and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))

        return dist



mat = [[0,0,0],[0,1,0],[0,0,0]]
print(updateMatrix(mat))