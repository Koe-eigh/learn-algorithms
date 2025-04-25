def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    a = [1, 1]
    for i in range(2, n+1):
        a.append(a[i-2]+a[i-1])
    return a[n]

if __name__ == "__main__":
    n = int(input())
    result = fibonacci(n)
    print(result)