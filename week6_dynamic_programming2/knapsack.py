# Uses python3
import sys

def optimal_weight(W, w):
    
    w.insert(0,0)
    dp = [[float("-inf")]*(W+1) for _ in range(len(w))]
    
    for i in range(len(w)):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j]
                if j >= w[i]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-w[i]]+w[i])
    
    return dp[len(w)-1][W]



if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
