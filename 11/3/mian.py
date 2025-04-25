# LCS: Longest Common Subsequence
def lengthOfLCS(str1: str, str2: str) -> int:
    m, n = len(str1), len(str2)
    c = [[0]*(n+1) for _ in range(m+1)]
    maximum = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
            maximum = max(maximum, c[i][j])
    return maximum

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        X = input()
        Y = input()
        result = lengthOfLCS(X, Y)
        print(result)