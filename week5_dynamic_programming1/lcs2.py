#Uses python3

import sys

def lcs2(a, b):
    a.insert(0,0)
    b.insert(0,0)
    n = len(a)
    m = len(b)
    dp = [[float("-inf")]*(n) for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif b[i] == a[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[m-1][n-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
