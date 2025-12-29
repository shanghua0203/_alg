import numpy as np
import itertools
import time

# --- 選手 1：蒙地卡羅積分 (亂撒豆子) ---
def monte_carlo_integration(func, bounds, num_samples=200000):
    # 準備邊界
    bounds = np.array(bounds)
    lower = bounds[:, 0]
    upper = bounds[:, 1]
    
    # 算出總體積
    volume = np.prod(upper - lower)
    
    # 隨機產生點 (撒豆子)
    points = np.random.uniform(low=lower, high=upper, size=(num_samples, len(bounds)))
    
    # 算出高度並取平均
    values = np.apply_along_axis(func, 1, points)
    avg_height = np.mean(values)
    
    return volume * avg_height

# --- 選手 2：黎曼積分 (乖乖切塊) ---
def riemann_integration(func, bounds, cuts_per_dim=50):
    """
    cuts_per_dim: 每一邊切幾刀。
    注意：如果維度很高，這個數字稍微大一點，電腦就會當機。
    例如 5 維，切 20 刀，就是 20^5 = 320 萬個點。
    """
    bounds = np.array(bounds)
    n_dim = len(bounds)
    
    # 1. 計算每一小塊的體積 (dV)
    # 每一維的長度除以切割數，再乘起來
    steps = (bounds[:, 1] - bounds[:, 0]) / cuts_per_dim
    dV = np.prod(steps)
    
    # 2. 產生網格點 (這是最耗效能的地方！)
    # 這裡用了 itertools.product 來產生所有座標組合
    ranges = [np.linspace(b[0], b[1], cuts_per_dim, endpoint=False) + s/2 for b, s in zip(bounds, steps)]
    # 加上 s/2 是為了取每一小塊的「中心點」來算，比較準 (中點法則)
    
    print(f"  [黎曼選手] 準備產生 {cuts_per_dim**n_dim} 個格子點並計算中...")
    
    total_value = 0
    # 3. 跑回圈一個一個加 (或是用矩陣運算加速)
    # 為了模擬「逐個掃描」的感覺，這裡用生成器轉成陣列運算
    # 建立所有點的座標矩陣
    grid_points = np.array(list(itertools.product(*ranges)))
    
    # 帶入函數計算
    values = np.apply_along_axis(func, 1, grid_points)
    
    # 總和 * 小體積
    return np.sum(values) * dV

# --- 比賽題目 ---
# 我們算一個 4 維的球體積 (Hyper-sphere)
# 只要點到圓心的距離 <= 1，高度就是 1，否則高度就是 0
# 理論上 半徑為 1 的 4 維球體積公式是: (pi^2) / 2 ≈ 4.9348
def hypersphere_func(point):
    # 如果 x1^2 + x2^2 + ... <= 1 回傳 1，否則回傳 0
    if np.sum(point**2) <= 1:
        return 1
    else:
        return 0

# --- 開始比賽 ---

# 設定 4 維，範圍都在 -1 到 1 之間
dim = 4
bounds = [(-1, 1)] * dim 
exact_answer = (np.pi**2) / 2  # 正確答案約 4.9348

print(f"=== 比賽開始：計算 {dim} 維球體積 ===")
print(f"正確標準答案應該是: {exact_answer:.5f}\n")

# 1. 蒙地卡羅的回合
start_t = time.time()
mc_ans = monte_carlo_integration(hypersphere_func, bounds, num_samples=300000)
end_t = time.time()
print(f"【蒙地卡羅 (撒30萬顆豆)】")
print(f"答案: {mc_ans:.5f}")
print(f"耗時: {end_t - start_t:.4f} 秒")
print(f"誤差: {abs(mc_ans - exact_answer):.5f}")
print("-" * 30)

# 2. 黎曼積分的回合
# 4 維如果要產生跟蒙地卡羅差不多的運算量 (30萬次)，每一邊只能切約 23 刀 (23^4 ≈ 28萬)
cuts = 23 
start_t = time.time()
rm_ans = riemann_integration(hypersphere_func, bounds, cuts_per_dim=cuts)
end_t = time.time()
print(f"【黎曼積分 (每邊切{cuts}刀, 共{cuts**dim}個點)】")
print(f"答案: {rm_ans:.5f}")
print(f"耗時: {end_t - start_t:.4f} 秒")
print(f"誤差: {abs(rm_ans - exact_answer):.5f}")