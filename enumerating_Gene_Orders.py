n = int(input())

arr = []

def numb(arr):
    d = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
    for i in arr:
        d[i] += 1
        if d[i] > 1:
            return False
    return True


nu = 0

def generate(k, prefix):
    if k == 0:
        if numb(prefix):
            arr.append(prefix[0])
            print(*prefix)
    else:
        for i in range(n):
            prefix.append(i + 1)
            generate(k - 1, prefix)
            prefix.pop()


generate(n, [])

print(len(arr))