from collections import deque
def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        rows = len(image)
        cols = len(image[0])
        start = image[sr][sc]
        if start == color :
            return image

        q = deque()
        q.append((sr,sc))

        image[sr][sc] = color

        direction = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            x,y = q.popleft()

            for dx,dy in direction:
                nx = x + dx 
                ny = y + dy 

                if 0<=nx<rows and 0<=ny<cols and image[nx][ny] == start:
                    image[nx][ny] = color
                    q.append((nx,ny))

        return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(floodFill(image, sr, sc, color))