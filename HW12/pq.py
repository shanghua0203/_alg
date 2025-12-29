import numpy as np

# 1. 設定真相 (True Distribution p)
p = np.array([0.7, 0.3])

# 2. 設定初始猜測 (Initial q) - 隨便猜一個跟真相差很多的
# 我們使用「權重」再透過 softmax 轉成機率，確保機率和永遠為 1
w = np.array([0.1, 0.9]) 

learning_rate = 0.1  # 每次移動的步長
iterations = 1000     # 走 100 步

print(f"開始尋找最低點...")
print(f"真實答案 p: {p}")
print("-" * 30)

for i in range(iterations):
    # 將權重轉換為機率 q (使用 Softmax 確保 q1 + q2 = 1)
    exp_w = np.exp(w)
    q = exp_w / np.sum(exp_w)
    
    # 計算目前的交叉熵 H(p, q)
    loss = -np.sum(p * np.log(q + 1e-9)) # 加 1e-9 是為了防止 log(0)
    
    # 計算梯度 (這就是「下坡」的方向)
    # 數學證明過，這個方向就是 (q - p)
    gradient = q - p
    
    # 往坡度低的地方走一步
    w = w - learning_rate * gradient
    
    # 每 20 步印出一次結果觀察
    if i % 20 == 0:
        print(f"第 {i:3} 步 | 目前猜測 q: {q.round(4)} | 損失(扣分): {loss:.4f}")

print("-" * 30)
print(f"最終結果 q: {q.round(4)}")
print(f"證明成功：q 是否等於 p？ {'是的！' if np.allclose(q, p, atol=0.01) else '還差一點'}")