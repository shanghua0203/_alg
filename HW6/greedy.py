import random
import time

# 題目設定：我們有一些奇怪的硬幣，要湊出目標金額
# 這種組合是貪婪法的剋星 (Greedy 會拿 5，剩 1，無法找錢)
COINS = [5, 2] 
TARGET_AMOUNT = 6

def greedy_solver(coins, amount):
    """
    第一關：貪婪法
    策略：每次都拿「最大的」硬幣
    """
    # 先從大排到小
    sorted_coins = sorted(coins, reverse=True)
    result = []
    current = amount
    
    for coin in sorted_coins:
        while current >= coin:
            current -= coin
            result.append(coin)
            
    if current == 0:
        return result
    else:
        return None  # 找不出來 (比如剩下 1 元)

def randomized_greedy_solver(coins, amount, max_retries=100):
    """
    第二關：隨機貪婪法
    策略：每次隨機從「可用的」硬幣裡挑一個，試很多次碰運氣
    """
    for i in range(max_retries):
        result = []
        current = amount
        
        # 單次嘗試的迴圈
        while current > 0:
            # 找出目前所有能用的硬幣 (比剩餘金額小的)
            valid_coins = [c for c in coins if c <= current]
            if not valid_coins:
                break # 死胡同，這次失敗
            
            # 【關鍵】隨機挑一個，而不是挑最大的
            pick = random.choice(valid_coins)
            current -= pick
            result.append(pick)
            
        if current == 0:
            print(f"   -> 在第 {i+1} 次嘗試時幸運找到了！")
            return result

    return None # 試了這麼多次都沒用，放棄

def dp_solver(coins, amount):
    """
    第三關：動態規劃 (Dynamic Programming)
    策略：地毯式計算，建立表格 (Table)，保證找到最佳解
    """
    # dp[i] 代表湊出金額 i 最少需要幾個硬幣
    # 初始化一個很大的數代表無法湊出
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # 用來記錄路徑，方便最後回推是拿了哪些硬幣
    parent = [-1] * (amount + 1) 
    chosen = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    parent[i] = i - coin
                    chosen[i] = coin
    
    if dp[amount] == float('inf'):
        return None
    
    # 回推路徑找出硬幣組合
    result = []
    curr = amount
    while curr > 0:
        result.append(chosen[curr])
        curr = parent[curr]
    
    return result

# --- 主程式執行流程 ---

print(f"題目：用硬幣 {COINS} 湊出 {TARGET_AMOUNT} 元\n")

# 1. 嘗試貪婪法
print("【第一階段】嘗試貪婪法 (Greedy)...")
ans = greedy_solver(COINS, TARGET_AMOUNT)

if ans:
    print(f"成功！貪婪法答案: {ans}")
else:
    print("失敗！貪婪法走進死胡同 (因為拿了 5，剩下 1 沒硬幣可找)。")
    print("-" * 30)

    # 2. 嘗試隨機貪婪法
    print("【第二階段】啟動隨機貪婪法 (Randomized Greedy)...")
    ans = randomized_greedy_solver(COINS, TARGET_AMOUNT)
    
    if ans:
        print(f"成功！隨機貪婪法答案: {ans}")
    else:
        print("失敗！運氣不好，試了一百次都沒找到。")
        print("-" * 30)

        # 3. 嘗試動態規劃
        print("【第三階段】啟動最終兵器：動態規劃 (Dynamic Programming)...")
        ans = dp_solver(COINS, TARGET_AMOUNT)
        
        if ans:
            print(f"成功！動態規劃答案: {ans}")
        else:
            print("無解！這個金額真的湊不出來。")