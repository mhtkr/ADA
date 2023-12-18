import time

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    L = [[None] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

print("Length of LCS is:", end=' ')
start = time.time()
print(lcs(str1, str2))
end = time.time()

print("Time taken for execution is", (end - start) * 1000, "ms")
