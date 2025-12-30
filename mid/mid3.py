import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 + 5*x

# 起點
x = 10
# 學習率
lr = 0.01

history_x = [x]
history_y = [f(x)]

#開始學習
for epoch in range(500):
    grad = 2 * x + 5  #x^2+5x 微分
    x = x - lr * grad #更新狀態
    
    history_x.append(x)
    history_y.append(f(x))
    
    if (epoch % 50) == 0:
        print(f"第 {epoch+1} 步 x: {x:.4f}")
print(f"最後停在 x={x:.2f}")

# --- 畫圖由AI產生---
# 畫出藍色的曲線（山坡的樣子）
curve_x = np.linspace(-6, 2, 100) # 產生從 -6 到 2 的一堆點
curve_y = f(curve_x)

plt.figure(figsize=(10, 6))
plt.plot(curve_x, curve_y, 'b-', label='Function Curve ($x^2 + 5x$)')

# 畫出紅色的點和線（球滾動的路徑）
plt.plot(history_x, history_y, 'ro-', markersize=2, linewidth=1, alpha=0.5, label='Learning Path')

# 標出起點和終點
plt.plot(history_x[0], history_y[0], 'go', markersize=10, label='Start (x=1)')
plt.plot(history_x[-1], history_y[-1], 'yo', markersize=10, label='End (Result)')

plt.title("Gradient Descent Visualization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()