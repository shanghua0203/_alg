# 1. 這是我們要找最低點的函數 (像一個碗)
def f(x):
    return x ** 2

# 2. 這是計算「斜率」的工具 (微分)
# 概念：把 x 往右動一點點，看高度變化多少
def get_slope(x):
    step = 0.001
    return (f(x + step) - f(x)) / step

# 3. 梯度下降法主程式
def gradient_descent():
    # 起始位置：隨便選一個地方開始 (例如 x = 10)
    current_x = 10.0
    
    learning_rate = 0.1  # 學習率：每次要跨多大步
    epochs = 100         # 總共要走幾步
    
    print(f"從 x = {current_x} 開始下山...")

    for i in range(epochs):
        # 看一下現在這點的斜率是多少
        slope = get_slope(current_x)
        
        # 往「斜率相反」的方向走一小步
        # 如果斜率是正的(往右爬)，我們就往左走(減法)
        current_x = current_x - (learning_rate * slope)
        
        # 每走 10 步印一下進度
        if i % 10 == 0:
            print(f"第 {i} 步：我現在在 x = {current_x:.4f}，這裡的高度是 {f(current_x):.4f}")

    return current_x

# 執行下山任務
final_x = gradient_descent()
print("-" * 30)
print(f"大功告成！找到的最低點大約在 x = {final_x:.4f}")