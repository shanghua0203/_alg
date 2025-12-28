# 這是棋盤的大小，8皇后就是 8
N = 8
# 這裡存皇后的位置，board[row] = col 表示第 row 行的皇后在第 col 列
board = [-1] * N
count = 0 # 算算有幾種解法

def is_safe(row, col):
    """檢查這個位置 (row, col) 會不會被攻擊"""
    for prev_row in range(row):
        prev_col = board[prev_row]
        # 1. 檢查垂直線：是不是在同一列
        if prev_col == col:
            return False
        # 2. 檢查對角線：行距是否等於列距 (斜率概念)
        if abs(row - prev_row) == abs(col - prev_col):
            return False
    return True

def solve_n_queens(row):
    global count
    # 【終止條件】如果已經走到第 9 行 (row == N)，表示 8 個都放好了！
    if row == N:
        count += 1
        return

    # 【暴力嘗試】從第 0 列試到第 7 列
    for col in range(N):
        if is_safe(row, col):
            # 1. 佔位：把皇后放下去
            board[row] = col 
            
            # 2. 深度優先 (DFS)：直接殺去下一行
            solve_n_queens(row + 1)
            
            # 3. 回溯：如果上面那行 return 回來了，表示那條路走完（或走不通）了
            # 迴圈會繼續跑，嘗試下一個 col，這就是「退一步換個位置」
            board[row] = -1 

# 開始執行
solve_n_queens(0)
print(f"總共找到了 {count} 種解法！")