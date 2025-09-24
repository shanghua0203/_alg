#!/usr/bin/env python3
"""
truth_table_enumerate.py

用法範例：
    python truth_table_enumerate.py -n 3
    python truth_table_enumerate.py --names A,B,C --format bool
    python truth_table_enumerate.py -n 4 --format bit

說明：
  這個程式使用 itertools.product 列舉出 n 個布林變數的所有可能輸入（truth-table 左半部），
  支援以 0/1 或 True/False 顯示，並可自訂變數名稱。

作者：ChatGPT
"""

import argparse
from itertools import product
import sys


def generate_truth_table(n, names=None, display_bool=False):
    """產生並回傳一個真值表（只含輸入列舉）

    參數:
      n: 變數數量（int）
      names: 變數名稱清單（list of str）或 None
      display_bool: 若為 True 則用 True/False，否則用 1/0

    回傳:
      header (list of str), rows (list of tuple)
    """
    if names:
        if len(names) != n:
            raise ValueError("變數名稱數量必須等於 n")
    else:
        names = [f"V{i+1}" for i in range(n)]

    # 使用 itertools.product 列舉所有 0/1 組合
    rows = list(product([0, 1], repeat=n))

    if display_bool:
        rows = [tuple(bool(x) for x in r) for r in rows]

    return names, rows


def pretty_print_table(header, rows, spacing=4):
    """將表格美觀地印出到 stdout"""
    # 決定每欄寬度：取欄名與欄內項目最大長度
    n_cols = len(header)
    col_widths = [len(h) for h in header]
    for r in rows:
        for i, cell in enumerate(r):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # 建表頭
    sep = ' ' * spacing
    header_line = sep.join(h.ljust(col_widths[i]) for i, h in enumerate(header))
    print(header_line)
    print('-' * len(header_line))

    # 建表身
    for r in rows:
        line = sep.join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(r))
        print(line)


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="列舉真值表左側（所有輸入組合）")
    p.add_argument('-n', '--num', type=int, default=3,
                   help='變數個數（預設 3）')
    p.add_argument('--names', type=str, default=None,
                   help='以逗號分隔的變數名稱，例如 A,B,C （數量必須等於 -n）')
    p.add_argument('--format', choices=['bit', 'bool'], default='bit',
                   help='顯示格式：bit (0/1) 或 bool (True/False)，預設 bit')
    return p.parse_args(argv)


if __name__ == '__main__':
    args = parse_args()
    n = args.num
    if n < 1:
        print('變數數量必須 >= 1', file=sys.stderr)
        sys.exit(1)

    names = None
    if args.names:
        names = [name.strip() for name in args.names.split(',') if name.strip()]

    try:
        header, rows = generate_truth_table(n, names=names, display_bool=(args.format == 'bool'))
    except ValueError as e:
        print('錯誤：', e, file=sys.stderr)
        sys.exit(2)

    pretty_print_table(header, rows)

# 範例輸出（當 n=3, format=bit）
# V1 V2 V3
# ----------
# 0  0  0
# 0  0  1
# 0  1  0
# 0  1  1
# 1  0  0
# 1  0  1
# 1  1  0
# 1  1  1
