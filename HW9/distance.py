def min_edit_with_reasoning(s1, s2):
    len1, len2 = len(s1), len(s2)
    # 建立表格
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    # 初始化基礎分數
    for i in range(len1 + 1): dp[i][0] = i
    for j in range(len2 + 1): dp[0][j] = j

    print(f"開始推導：要把 '{s1}' 變成 '{s2}'\n")

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            char1, char2 = s1[i-1], s2[j-1]
            print(f"--- 正在檢查：'{char1}' (來自{s1}) 和 '{char2}' (來自{s2}) ---")

            if char1 == char2:
                # 字母相同，直接抄左上角
                dp[i][j] = dp[i-1][j-1]
                print(f"  [結果] 字母一模一樣！不用動手，直接抄左上角的答案：{dp[i][j]}")
            else:
                # 字母不同，看鄰居
                replace = dp[i-1][j-1]
                delete = dp[i-1][j]
                insert = dp[i][j-1]
                
                best_option = min(replace, delete, insert)
                dp[i][j] = 1 + best_option
                
                print(f"  [推理] 字母不同。我看了鄰居的分數：")
                print(f"         - 想用『取代』的話，之前是 {replace} 次")
                print(f"         - 想用『刪除』的話，之前是 {delete} 次")
                print(f"         - 想用『插入』的話，之前是 {insert} 次")
                print(f"  [結果] 我選最省力的 {best_option}，再加上這次的動作，這格填入：{dp[i][j]}")
            print()

    print("--- 推導結束，最終計分表如下 ---")
    for row in dp:
        print(row)
    
    return dp[len1][len2]

# 用簡單的例子來跑跑看
min_edit_with_reasoning("cat", "cut")