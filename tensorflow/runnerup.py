num = str(input())
[int(i) for i in str(num)]
n = sorted(num, reverse=True)
print(n)

if n[0] > n[1]:
    print(n[1])
else:
    buf = 0
    for j in n:
        if n[buf] < n[0]:
            print(n[buf])
            break
        else:
            buf += 1
