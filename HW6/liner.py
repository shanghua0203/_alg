import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 步驟 1: 產生隨機的範例資料
# 讓我們的資料點在 x 軸上從 0 到 2 之間隨機分佈
np.random.seed(0) # 讓每次產生的隨機資料都一樣，方便重現結果
X = 2 * np.random.rand(100, 1)
# y 跟 X 有線性關係 (y = 4 + 3x)，再加上一些雜訊，讓它更真實
y = 4 + 3 * X + np.random.randn(100, 1)

# 步驟 2: 建立並訓練線性迴歸模型
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# 步驟 3: 畫出結果
plt.figure(figsize=(8, 6))
# 畫出原始的資料點 (散佈圖)
plt.scatter(X, y, alpha=0.6, label="原始資料點")

# 畫出模型找到的迴歸線
# 我們取 x=0 和 x=2 兩個點，讓模型預測 y 值，然後連成一線
X_new = np.array([[0], [2]])
y_predict = lin_reg.predict(X_new)
plt.plot(X_new, y_predict, "r-", linewidth=2, label="迴歸線")

# 加上繁體中文的圖表標題和標籤
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # 設定字體為微軟正黑體
plt.rcParams['axes.unicode_minus'] = False # 解決負號顯示問題
plt.title("Python 線性迴歸範例")
plt.xlabel("X 軸")
plt.ylabel("Y 軸")
plt.legend()
plt.grid(True)

# 儲存圖檔
plt.savefig("linear_regression_example.png")

print("圖片已儲存為 linear_regression_example.png")