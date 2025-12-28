import numpy as np
import matplotlib.pyplot as plt

# 步驟 1: 產生跟上次一樣的範例資料
# 固定的隨機種子讓每次產生的資料都相同，方便比較
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
# 我們的目標線是 y = 4 + 3x，加上一些雜訊
y = 4 + 3 * X + np.random.randn(100, 1)

# 步驟 2: 定義我們的「計分」函式 (計算誤差)
# 我們要最小化這個數值
def calculate_mse(m, b, X, y):
    """計算給定 m 和 b 的均方誤差 (Mean Squared Error)"""
    # 根據 y = mx + b 計算預測值
    y_pred = m * X + b
    # 計算實際值與預測值的差的平方的平均值
    error = np.mean((y - y_pred)**2)
    return error

# 步驟 3: 實作爬山演算法
def hill_climbing_for_regression(X, y, iterations=1000, step_size=0.01):
    """
    使用爬山演算法尋找最佳的 m 和 b
    """
    # 從一個隨機的斜率(m)和截距(b)開始
    current_m = np.random.randn()
    current_b = np.random.randn()
    best_error = calculate_mse(current_m, current_b, X, y)
    
    print(f"初始狀態 -> m: {current_m:.4f}, b: {current_b:.4f}, 誤差: {best_error:.4f}")

    # 開始「爬山」(其實是下山，因為要找最小值)
    for i in range(iterations):
        # 探索鄰居 (上下左右四個方向)
        neighbors = [
            (current_m + step_size, current_b), # 往右
            (current_m - step_size, current_b), # 往左
            (current_m, current_b + step_size), # 往上
            (current_m, current_b - step_size)  # 往下
        ]
        
        # 找出最好的鄰居
        best_neighbor_m, best_neighbor_b = current_m, current_b
        best_neighbor_error = best_error
        
        for m, b in neighbors:
            error = calculate_mse(m, b, X, y)
            if error < best_neighbor_error:
                best_neighbor_error = error
                best_neighbor_m, best_neighbor_b = m, b
        
        # 如果最好的鄰居比現在的位置還要好，就移動過去
        if best_neighbor_error < best_error:
            best_error = best_neighbor_error
            current_m, current_b = best_neighbor_m, best_neighbor_b
        else:
            # 如果周圍沒有更好的點，表示已達局部最佳解，可以提早結束
            print(f"在第 {i+1} 次迭代找到最佳解！")
            break
            
    print(f"最終結果 -> m: {current_m:.4f}, b: {current_b:.4f}, 誤差: {best_error:.4f}")
    return current_m, current_b

# 執行演算法，找出 m 和 b
found_m, found_b = hill_climbing_for_regression(X, y)

# 步驟 4: 畫出結果
plt.figure(figsize=(8, 6))
plt.scatter(X, y, alpha=0.6, label="原始資料點")

# 畫出爬山演算法找到的線
x_line = np.array([0, 2])
y_line = found_m * x_line + found_b
plt.plot(x_line, y_line, "r-", linewidth=2, label="爬山演算法找到的線")

# 加上繁體中文的圖表標題和標籤
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title("用爬山演算法解線性回歸")
plt.xlabel("X 軸")
plt.ylabel("Y 軸")
plt.legend()
plt.grid(True)
plt.savefig("hill_climbing_regression.png")

print("\n圖片已儲存為 hill_climbing_regression.png")