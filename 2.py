import sys
def main():
    n, m = map(int, input().split())
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            ways = 0
            if i >= 2 and j >= 1:
                ways += dp[i - 2][j - 1]
            if i >= 1 and j >= 2:
                ways += dp[i - 1][j - 2]
            dp[i][j] = ways
    print(dp[n - 1][m - 1])
if __name__ == '__main__':
    main()
