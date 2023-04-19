n = int(input())
a = list(map(int, input().split()))

D = [0]*n

D[0] = a[0]
D[1] = min(a[0], 0) + a[1]

for i in range(2, n):
    D[i] = min(D[i-1], D[i-2]) + a[i]
    
print(D[n-1])