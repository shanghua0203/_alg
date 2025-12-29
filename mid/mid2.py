import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1.資料點
x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([5, 4, 8, 9, 1])
y  = np.array([6, 7, 8, 8, 9])

# 2.隨便給一些初始的狀態
w1, w2, b = 0.0, 0.0, 0.0

# 學習率
lr = 0.0001

# 3. 開始學習（梯度下降）
for epoch in range(100000):
    y_pred = w1*x1 + w2*x2 + b
    
    # 計算梯度
    dw1 = -2 * sum(x1 * (y - y_pred))
    dw2 = -2 * sum(x2 * (y - y_pred))
    db  = -2 * sum(y - y_pred)
    
    # 更新狀態
    w1 -= lr * dw1
    w2 -= lr * dw2
    b  -= lr * db
    
    if (epoch % 1000) == 0:
        print(f"第 {epoch+1} 步 w1: {w1:.4f},w2: {w2:.4f},b: {b:.4f}")

# ===以下作圖由AI協助完成===

#  繪製 3D 結果
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 畫出原始的資料點 (散佈圖)
ax.scatter(x1, x2, y, color='red', s=100, label='Actual Data')

# 畫出電腦學到的平面
X1, X2 = np.meshgrid(np.linspace(1, 5, 10), np.linspace(1, 9, 10))
Y_plane = w1 * X1 + w2 * X2 + b
ax.plot_surface(X1, X2, Y_plane, alpha=0.5, color='cyan')

ax.set_xlabel('Study Hours (x1)')
ax.set_ylabel('Attendance (x2)')
ax.set_zlabel('Grade (y)')
plt.title("3D Gradient Descent: Finding the Best Plane")
plt.show()

print(f"學出的公式: Grade = ({w1:.2f})*x1 + ({w2:.2f})*x2 + {b:.2f}")