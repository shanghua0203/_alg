import random

# 1. 準備資料 (氣溫 x, 實際營收 y)
# 這裡簡單放 5 個點作為代表
x_data = [20, 25, 30, 35, 40]
y_data = [2000, 2500, 3100, 3400, 4100]

# 2. 定義「誤差」（損失函數）
# 這裡計算的是「預測值」跟「實際值」差了多少的平方和 (越多代表越不準)
def get_loss(a, b):
    total_error = 0
    for i in range(len(x_data)):
        prediction = a * x_data[i] + b  # 我們畫出的線算出來的答案
        actual = y_data[i]              # 真正的答案
        total_error += (prediction - actual) ** 2
    return total_error / len(x_data)

# 3. 爬山演算法
def hill_climbing():
    # 隨機給一個起點 (猜一個斜率 a 和 截距 b)
    current_a = random.uniform(-10, 10)
    current_b = random.uniform(-10, 10)
    
    step_size = 0.1  # 每次調整的一小步
    fail_count = 0   # 失敗計數器
    
    while fail_count < 10000:  # 如果試了一萬次都沒辦法更準，就停止
        current_loss = get_loss(current_a, current_b)
        
        # 隨機動一點點 a 或 b
        next_a = current_a + random.uniform(-step_size, step_size)
        next_b = current_b + random.uniform(-step_size, step_size)
        
        next_loss = get_loss(next_a, next_b)
        
        # 如果新的誤差更小 (更準了)，就搬家過去！
        if next_loss < current_loss:
            current_a = next_a
            current_b = next_b
            fail_count = 0  # 成功了，失敗計數歸零
            # print(f"目前誤差: {next_loss:.2f} (a={current_a:.2f}, b={current_b:.2f})")
        else:
            fail_count += 1 # 沒變準，算失敗一次
            
    return current_a, current_b

# 執行找答案
best_a, best_b = hill_climbing()

print("--- 搜尋完成 ---")
print(f"找到的最準公式是: y = {best_a:.2f} * x + {best_b:.2f}")
print(f"最終誤差: {get_loss(best_a, best_b):.2f}")

# 4. 驗證：如果明天 32 度，預測營收是多少？
temp = 32
prediction = best_a * temp + best_b
print(f"預測氣溫 {temp} 度時，營收約為: {prediction:.2f} 元")