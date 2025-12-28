import random

# 這是我們要爬的山 (這座山可能有很多小山丘)
def f(x, y):
    # 這是一個數學公式，想像它是地圖的高度
    return -1 * (x**2 + y**2 + random.uniform(-1, 1)) 

# --- 基礎爬山法 ---
def hill_climbing(x, y):
    while True:
        current_height = f(x, y)
        # 往旁邊跨出一小步 (隨機動一點點)
        dx = random.uniform(-0.1, 0.1)
        dy = random.uniform(-0.1, 0.1)
        
        # 如果旁邊比較高，就移過去
        if f(x + dx, y + dy) > current_height:
            x, y = x + dx, y + dy
        else:
            # 如果旁邊都比較低，代表到山頂了，停下來
            return x, y, current_height

# --- 改良法：隨機重新開始 (主程式) ---
def main():
    best_x, best_y = 0, 0
    global_highest = -1000000 # 先設一個極小的數字
    
    print("開始派人去爬山...")
    
    # 改良重點：我們重複試 1000 次！
    for i in range(1000):
        # 隨機空降一個起始位置
        start_x = random.uniform(-10, 10)
        start_y = random.uniform(-10, 10)
        
        # 叫這個人去爬山
        res_x, res_y, res_height = hill_climbing(start_x, start_y)
        
        # 如果這個人爬到的高度，比目前紀錄的還要高，就更新最高紀錄
        if res_height > global_highest:
            global_highest = res_height
            best_x, best_y = res_x, res_y
            print(f"第 {i} 次嘗試：發現更高的山頂！高度 = {global_highest:.2f}")

    print("-" * 20)
    print(f"最終大贏家：座標 ({best_x:.2f}, {best_y:.2f}) 高度 {global_highest:.2f}")

main()