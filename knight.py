from collections import deque

N = int(input()) 
raw_x, raw_y = map(int, input().split())

if N <= 2:
    print(0) 
    exit()


chess_board = [[-1 for _ in range(N)] for _ in range(N)]
start_x, start_y = raw_x, raw_y

if not (0 <= start_x < N and 0 <= start_y < N):
    for row in chess_board:
        print(row)
    print(0)
    exit()
q = deque()
dir_moves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)] 
num_squares_path_found = 0
chess_board[start_x][start_y] = 0 
q.append((start_x, start_y))
num_squares_path_found = 1 
while q:
    curr_x, curr_y = q.popleft()
    current_dist = chess_board[curr_x][curr_y]
    num_squares_path_found = current_dist
    f=0
    for dx, dy in dir_moves:
        nx, ny = curr_x + dx, curr_y + dy

        if 0 <= nx < N and 0 <= ny < N and chess_board[nx][ny] == -1:
            f=1
            chess_board[nx][ny] = current_dist + 1
            q.append((nx, ny))
            num_squares_path_found += 1
for row in chess_board:
    print(row)
print(num_squares_path_found)