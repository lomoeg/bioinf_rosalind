n = int(input())
K = 5

arr = []

def numb(arr):
    d = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, -1: 0, -2: 0, -3: 0, -4: 0, -5: 0, -6: 0, -7: 0}
    for i in arr:
        d[abs(i)] += 1
        if d[abs(i)] > 1 or i == 0:
            return False
    return True


def generate(k, prefix):
    if k == 0:
        if numb(prefix):
            arr.append(prefix[0])
            print(*prefix)
    else:
        for i in range(-n, n + 1):
            prefix.append(i)
            generate(k - 1, prefix)
            prefix.pop()


generate(n, [])

#print(numb([-1, 1, -1]))

print(len(arr))