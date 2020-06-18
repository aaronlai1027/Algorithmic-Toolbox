# Uses python3
import sys

def get_change(m):
    denominations = [1, 3, 4]
    dp = [float("inf")]*(m+1)
    dp[0] = 0
    for i in range(1,m+1):
        for den in denominations:
            if m >= den:
                dp[i]  = min(dp[i],dp[i-den]+1)
    return dp[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
