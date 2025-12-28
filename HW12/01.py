import math
import sys

sys.stdout.reconfigure(encoding='utf-8')


def sigmoid(x):
    # 這是一個把數字壓縮到 0~1 之間的函數 (用來產生機率 q)
    return 1 / (1 + math.exp(-x))

# --- 設定環境 ---
print("--- 訓練開始：教電腦學會認貓 ---")

# 1. 真實答案 (p)：這是一隻貓，所以是 1.0
p_true = 0.2 

# 2. 輸入特徵 (x)：假設這張圖片的一個特徵值 (例如耳朵尖尖的程度)
input_feature = 0.3

# 3. 初始參數 (weight)：電腦一開始隨便選的「權重」，代表它還很笨
weight = -0.5  # 隨便給一個負數，故意讓它一開始猜錯
learning_rate = 0.1 # 學習率：下山的腳步大小

# --- 開始訓練循環 (重複 20 次) ---
for epoch in range(1, 10000):
    # A. 前向傳播 (電腦試著猜測 q)
    # 預測值 = 輸入 * 權重
    z = input_feature * weight 
    q_pred = sigmoid(z) # 把結果變成 0~1 的機率
    
    # B. 計算損失 (Cross Entropy)
    # 套用公式： -[p * log(q) + (1-p) * log(1-q)]
    # 因為 p=1，公式簡化為 -log(q)
    loss = -math.log(q_pred)
    
    # C. 反向傳播 (計算梯度/斜坡方向)
    # 這裡省略複雜的微積分證明，對於 Cross Entropy + Sigmoid，
    # 梯度的公式剛好是： (預測值 - 真實值) * 輸入
    gradient = (q_pred - p_true) * input_feature
    
    # D. 更新參數 (往山谷走一步)
    # 新權重 = 舊權重 - (學習率 * 梯度)
    weight = weight - (learning_rate * gradient)
    
    # --- 印出目前的進度 ---
    # 我們每隔 5 次印出來看一下
    if epoch % 5 == 0 or epoch == 1:
        print(f"第 {epoch:2} 次訓練 | "
              f"預測機率(q): {q_pred:.4f} (目標是1.0) | "
              f"損失(Loss): {loss:.4f} | "
              f"權重變為: {weight:.4f}")

print("--- 訓練結束 ---")
print(f"最終結果：第 {epoch:2} 次訓練 "
      f"預測機率(q) = {q_pred:.4f}"
      f"損失 = {loss:.4f}，"
      f"權重 = {weight:.4f}，"        
        )