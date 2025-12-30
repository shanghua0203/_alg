# 方法 1
def power2n(n):
    return 2**n

# 方法 2a：用遞迴
def power2n2a(n):
    if  n == 0:
        return 1
    if n == 2:
        return 2
    return power2n2a(n-1)+power2n2a(n-1)
    # power2n(n-1)+power2n(n-1)

# 方法2b：用遞迴
def power2n2b(n):
    if  n == 0:
        return 1
    if n == 2:
        return 2
    return 2*power2n2b(n-1)
    #2*power2n(n-1)

# 方法 3：用遞迴+查表
def power2n3(n, memo={}):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = power2n3(n-1, memo) + power2n3(n-1, memo)
    return memo[n]

if __name__ == '__main__':
    n=4
    print(power2n(n))
    print(power2n2a(n))
    print(power2n2b(n))
    print(power2n3(n, memo={}))
