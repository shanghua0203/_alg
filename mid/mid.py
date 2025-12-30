import numpy as np
import matplotlib.pyplot as plt

# 1.資料點
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 2, 3, 3, 1])

# 2.隨便給一些初始的狀態
w = 0.0 
b = 0.0  

# 學習率
lr = 0.001 

# 3. 開始學習（梯度下降）
for epoch in range(1000):
    # 預測值
    y_pred = w * x + b
    
    # 計算梯度 2x+y
    w_grad = -2 * sum(x * (y - y_pred))
    b_grad = -2 * sum(y - y_pred)
    
    # 更新狀態
    w = w - lr * w_grad
    b = b - lr * b_grad
    
    if (epoch % 50) == 0:
        print(f"第 {epoch+1} 步 w: {w:.4f}, b: {b:.4f}")
print(f"W = {w:.2f}")

# 畫圖看結果
plt.scatter(x, y, color='red') # 原始的點
plt.plot(x, w * x + b)         # 電腦學會畫出的線
plt.show()

