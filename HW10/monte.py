import numpy as np

def monte_carlo_integration(func, bounds, num_samples=500000):
    """
    參數說明：
    func: 你想積分的那個函數 (要把一堆座標丟進去算出一個值)
    bounds: 每一維的範圍，例如 [(0, 1), (0, 1)] 代表二維，每一維都在 0 到 1 之間
    num_samples: 撒豆子的數量，預設 50 萬顆 (越多越準)
    """
    
    # 1. 準備工作
    bounds = np.array(bounds)
    lower_bounds = bounds[:, 0] # 每一維的下限
    upper_bounds = bounds[:, 1] # 每一維的上限
    n_dim = len(bounds)         # 總共有幾維 (n)

    # 2. 算出那個「大盒子」的體積
    # 就是把每一維的長度 (上限 - 下限) 全部乘起來
    volume = np.prod(upper_bounds - lower_bounds)

    # 3. 開始亂撒豆子 (產生隨機點)
    # 產生 num_samples 個點，每個點有 n_dim 個座標
    points = np.random.uniform(low=lower_bounds, high=upper_bounds, size=(num_samples, n_dim))

    # 4. 算出所有豆子的函數值，然後取平均 (平均高度)
    # axis=1 代表把每個點的座標一起傳進去算
    values = np.apply_along_axis(func, 1, points)
    average_height = np.mean(values)

    # 5. 最終計算：體積 x 平均高度
    result = volume * average_height
    
    return result

# --- 測試區 (我們來試試看算不算得準) ---

# 定義一個函數： f(x) = x1^2 + x2^2 (這是一個 2 維的碗公形狀)
def my_function(point):
    return np.sum(point**2)

# 設定範圍：2 維，每一維都是 0 到 1
# 數學理論值應該是 2/3 (大約 0.6666...)
bounds_2d = [(0, 1), (0, 1)] 

# 執行積分
ans = monte_carlo_integration(my_function, bounds_2d)

print(f"程式算出來的答案: {ans}")
print(f"理論上的正確答案: {2/3}")