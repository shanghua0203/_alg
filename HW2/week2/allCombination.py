def combination(A, m): # 從 A 陣列中取出 m 個的所有可能性
	chooses = []
	c(A, len(A), m, chooses, m)

def c(A, n, k, chooses, m): # 從 A[0..n] 中選取 k 個補進 chooses，如果滿 m 個就印出
	if len(chooses)==m:
		print(chooses)
		return
	if n <= 0: return
	c(A,n-1,k,chooses,m) # C(n-1,k) // A[n-1] 沒取到

	chooses.append(A[n-1])
	c(A,n-1,k-1,chooses,m) # C(n-1,k-1) // A[n-1] 有取到
	del chooses[-1]

combination([1,2,3,4,5], 3)

"""簡單明確的組合 (combinations) 產生器範例

提供一個可讀性較高的遞迴實作 `combinations(A, m)`，返回從列表 `A`
中選出 `m` 個元素的所有可能組合（每個組合為一個列表）。範例的 `main()`
會示範列印結果與總數。

說明重點：使用遞迴決定每個元素是「選」還是「不選」，累積到長度為 m 時加入結果。
"""

from typing import List


def combinations(A: List, m: int) -> List[List]:
	"""返回所有從 A 選出 m 個元素的組合。

	參數:
	- A: 原始序列（例如 list）
	- m: 要選出的元素數量（m >= 0）

	回傳:
	- list of lists: 每個子列表為一個組合，保留 A 中元素的相對順序
	"""
	result = []

	def backtrack(start: int, path: List):
		# 如果目前 path 長度達到 m，複製並加入結果
		if len(path) == m:
			result.append(path.copy())
			return

		# 從 start 開始選元素，避免重複與保持順序
		for i in range(start, len(A)):
			path.append(A[i])
			backtrack(i + 1, path)
			path.pop()

	# 提早處理不可能的情況
	if m < 0:
		raise ValueError("m must be non-negative")
	if m == 0:
		return [[]]
	if m > len(A):
		return []

	backtrack(0, [])
	return result


def main():
	A = [1, 2, 3, 4, 5]
	m = 3
	combs = combinations(A, m)
	for c in combs:
		print(c)
	print(f"Total: {len(combs)} combinations")


if __name__ == "__main__":
	main()

