K, n = map(int, input().split())

arr = []


def numb(arr):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        if d[i] > 1:
            return False
    return True


def generate(k, prefix):
    if k == 0:
        if numb(prefix):
            arr.append(prefix[0])
            print(*prefix)
    else:
        for i in range(K):
            prefix.append(i)
            generate(k - 1, prefix)
            prefix.pop()


generate(n, [])

#print(numb([-1, 1, -1]))

print(len(arr))