n, m, d = map(int, input().split())
times = []
arr = []

for i in range(m):
    a, b, t = map(int, input().split())
    if t not in times:
        times.append(t)
        arr.append([0 for r in range(n)])
        if len(times) > 1:
            for x in range(n):
                maxd = d * (times[-1] - times[-2])
                start = max(0, x - maxd)
                end = min(n, x + maxd + 1)
                arr[-1][x] += max(arr[-2][start:end])
    for x in range(n):
        arr[-1][x] += (b - abs(a - (x + 1)))

print(max(arr[-1]))
