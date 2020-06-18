# Uses python3
def edit_distance(s, t):
    s = "#" + s
    t = "#" + t
    n = len(s)
    m = len(t)
    dp = [[float("inf")]*(n) for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = i
    for j in range(n):
        dp[0][j] = j

    for i in range(1,m):
        for j in range(1,n):
            insert = dp[i][j-1] + 1
            delete = dp[i-1][j] + 1
            match = dp[i-1][j-1]
            mismatch = dp[i-1][j-1] + 1
            if t[i] == s[j]:
                dp[i][j] = min(insert,delete,match)
            else:
                dp[i][j] = min(insert,delete,mismatch)
    return dp[m-1][n-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
