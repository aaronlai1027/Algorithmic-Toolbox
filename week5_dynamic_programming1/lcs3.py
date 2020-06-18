#Uses python3

import sys

def lcs3(a, b, c):
    a.insert(0,0)
    b.insert(0,0)
    c.insert(0,0)
    n = len(a)
    m = len(b)
    l = len(c)
    dp = [[[float("-inf")]*(n) for _ in range(m)] for _ in range(l)]

    for i in range(l):
        for j in range(m):
            for k in range(n):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                elif c[i] == b[j] == a[k]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
    return dp[l-1][m-1][n-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
