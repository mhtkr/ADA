import time

def MatChainMul(arr, n):
    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(1, n):
        dp[i][i] = 0

    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i + L - 1
            dp[i][j] = 10**10

            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[1][n-1]

n = int(input("Enter the number of elements in the array: "))
arr = []

print("Enter the elements of the array:")
for i in range(0, n):
    el = int(input())
    arr.append(el)

print("Minimum number of multiplications are ", end="")
start = time.time()
print(MatChainMul(arr, n))
end = time.time()

print("Time taken for execution is", (end - start) * 1000, "ms")
